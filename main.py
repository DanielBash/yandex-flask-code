from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import Optional, DataRequired

app = Flask(__name__)
professions = 'Водопроводчик Ниндзя Тусовщица Анимешник Переводчик Стилист Продакт-менеджер Профессор-математики'.split()


class ProfileForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    education = TextAreaField('Образование')
    profession = StringField('Профессия', validators=[DataRequired()])
    sex = SelectField('Пол', choices=[('male', 'Мужчина'), ('female', 'Женщина')], validators=[DataRequired()])
    motivation = TextAreaField('Мотивация')
    ready = BooleanField('Готовы ли вы остаться на марсе?')


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
        return redirect(url_for('index', title='Форма отправлена'))
    return render_template('answer.html', form=form)


@app.route('/auto_answer', methods=['GET'])
def auto_answer():
    print(session['form_data'])
    return render_template('auto_answer.html', data={
        'ФАМИЛИЯ': session['form_data']['surname'],
        'ИМЯ': session['form_data']['name'],
        'МОТИВАЦИЯ': session['form_data']['motivation'],
        'ПРОФЕССИЯ': session['form_data']['profession'],
        'ПОЛ': session['form_data']['sex'],
        'ОБРОЗАВАНИЕ': session['form_data']['education'],
        'ГОТОВ ОСТАТЬСЯ?': session['form_data']['ready'],
    })


if __name__ == '__main__':
    app.secret_key = 'super-secure-secret-key'
    app.run(host='0.0.0.0', port=8080)
