import colorsys

from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
professions = 'Водопроводчик Ниндзя Тусовщица Анимешник Переводчик Стилист Продакт-менеджер Профессор-математики'.split()
all_users = []


def generate_color(sex, age):
    if sex.lower().startswith('f'):
        hue = 0.0
    elif sex.lower().startswith('m'):
        hue = 4.0 / 6.0
    else:
        hue = 0.0

    saturation = max(0.3, 1.0 - (int(age) / 100.0))
    value = 0.8

    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

    return '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))


class ProfileForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    education = TextAreaField('Образование')
    profession = StringField('Профессия', validators=[DataRequired()])
    sex = SelectField('Пол', choices=[('male', 'Мужчина'), ('female', 'Женщина')], validators=[DataRequired()])
    motivation = TextAreaField('Мотивация')
    password = StringField('Пароль', validators=[DataRequired()])
    ready = BooleanField('Готовы ли вы остаться на марсе?')


class LoginForm(FlaskForm):
    capitan_id = StringField('ID капитана', validators=[DataRequired()])
    capitan_pass = StringField('Пароль капитана', validators=[DataRequired()])
    user_id = StringField('ID пользователя', validators=[DataRequired()])
    user_pass = StringField('Пароль пользователя', validators=[DataRequired()])


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:prof>')
def training(prof):
    training_target = 'Научные симуляторы'
    if 'инженер' in prof or 'строитель' in prof:
        training_target = 'Инженерные тренажеры'
    return render_template('training.html', training_target=training_target)


@app.route('/list_prof/<string:display>')
def list_prof(display):
    if display not in ['ul', 'ol']:
        return f'Неверный параметр display: {display}.'
    return render_template('list_prof.html', display=display, professions=professions)


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    form = ProfileForm()
    if form.validate_on_submit():
        if not form.validate_on_submit():
            return redirect(url_for('index', title='ОШИБКА'))
        data = form.data
        session['form_data'] = data
        all_users.append(form.data)
        return redirect(url_for('index', title='Форма отправлена'))
    return render_template('answer.html', form=form)


@app.route('/auto_answer', methods=['GET'])
def auto_answer():
    return render_template('auto_answer.html', data={
        'ФАМИЛИЯ': session['form_data']['surname'],
        'ИМЯ': session['form_data']['name'],
        'МОТИВАЦИЯ': session['form_data']['motivation'],
        'ПРОФЕССИЯ': session['form_data']['profession'],
        'ПОЛ': session['form_data']['sex'],
        'ОБРОЗАВАНИЕ': session['form_data']['education'],
        'ГОТОВ ОСТАТЬСЯ?': session['form_data']['ready'],
    })


@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if not form.validate_on_submit():
            return redirect(url_for('index', title='ОШИБКА'))
        data = form.data
        return redirect(url_for('index', title='Форма отправлена'))
    return render_template('login.html', form=form)


@app.route('/distribution', methods=['GET'])
def distribution():
    return render_template('distribution.html', ppl=[{'capitan': True, 'name': 'Владимир Владимирович'},
                                                     {'capitan': False, 'name': 'Обама'},
                                                     {'capitan': False, 'name': 'Трамп'}])


@app.route('/table_param/<string:sex>/<int:age>', methods=['GET'])
def table(sex, age):
    color = generate_color(age=age, sex=sex)
    image_url = 'https://www.shutterstock.com/image-vector/cute-alien-bite-ufo-cartoon-600nw-2259840443.jpg'
    if age > 20:
        image_url = 'https://static.scientificamerican.com/dam/m/2a63d59b62cb6c52/original/Xenolinguistics_alien_lauguage.jpeg'

    return render_template('table.html', color=color, image_url=image_url)


if __name__ == '__main__':
    app.secret_key = 'super-secure-secret-key'
    app.run(host='0.0.0.0', port=8080)
