from flask import Flask, render_template

app = Flask(__name__)
professions = 'Водопроводчик Ниндзя Тусовщица Анимешник Переводчик Стилист Продакт-менеджер Профессор-математики'.split()


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


if __name__ == '__main__':
    app.secret_key = 'super-secure-secret-key'
    app.run(host='0.0.0.0', port=8080)
