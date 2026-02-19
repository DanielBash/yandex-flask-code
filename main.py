import os
from datetime import datetime

from flask import Flask, url_for, session, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'


@app.route('/promotion')
def promo():
    return '''Человечество вырастает из детства.<br/>

Человечеству мала одна планета.<br/>

Мы сделаем обитаемыми безжизненные пока планеты.<br/>

И начнем с Марса!<br/>

Присоединяйся!<br/>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
<title>Привет, Марс!</title>
</head>
<body>
<h1>Жди нас, Марс!</h1>
<img src="{url_for('static', filename='img/img.png')}"/>
<p>Марс - красный блин</p>
<div class="p-3 mb-2 alert-info" style="font-size: 30px">Человечество вырастает из дества</div>
<div class="p-3 mb-2 alert-success" style="font-size: 30px">Человечеству мала одна планета</div>
<div class="p-3 mb-2 alert-warning" style="font-size: 30px">Человечеству мала одна планета</div>
<div class="p-3 mb-2 alert-danger" style="font-size: 30px">Мы сделаем обитаемыми безжизенные пока планеты</div>
<div class="p-3 mb-2 alert-warning" style="font-size: 30px">И начнем с Марса!</div>
<div class="p-3 mb-2 alert-info" style="font-size: 30px">Присоединяйся!</div>
</body>
</html>'''


@app.route('/image_mars')
def image_mars():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Привет, Марс!</title>
</head>
<body>
<h1>Жди нас, Марс!</h1>
<img src="{url_for('static', filename='img/img.png')}"/>
<p>Марс - красный блин</p>
</body>
</html>'''


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="name" placeholder="Имя" name="name">
                                    <input type="text" class="form-control" id="surname" placeholder="Фамилия" name="surname">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Купленный диплом</option>
                                          <option>Палтос</option>
                                          <option>Забив</option>
                                        </select>
                                     </div>
                                     
                                     <div class="form-group">
                                        <label for="form-check">Какие у вас были профессии</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="choice" name="sex" id="male" checked>
                                          <label class="form-check-label" for="male">
                                            Инженер-Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="choice" name="sex" id="female">
                                          <label class="form-check-label" for="two">
                                            Инженер-Исследователь
                                          </label>
                                        </div>
                                    </div>
                                     
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите учавстовать в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                     
                                     <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                     
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на марсе</label>
                                    </div>
                                    
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


@app.route('/choice/<planet>')
def choice(planet):
    if planet == 'Марс':
        return f'''<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <title>Привет, {planet}!</title>
    </head>
    <body>
    <h1>Моё предложение: {planet}!</h1>
    <h2>Эта планета близка к земле;</h2>
    <div class="p-3 mb-2 alert-info" style="font-size: 30px">Эта планета близка к земле</div>
    <div class="p-3 mb-2 alert-success" style="font-size: 30px">На ней вода и отмосфера</div>
    <div class="p-3 mb-2 alert-warning" style="font-size: 30px">На ней небольшое магнитное поле</div>
    <div class="p-3 mb-2 alert-danger" style="font-size: 30px">Наконец, она просто красива</div>
    </body>
    </html>'''
    else:
        return f'''<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <title>Привет, {planet}!</title>
    </head>
    <body>
    <h1>Моё предложение: {planet}!</h1>
    <img src="{url_for('static', filename='img/img.png')}"/>
    <p>Марс - красный блин</p>
    <div class="p-3 mb-2 alert-info" style="font-size: 30px">Ничего не изветсно</div>
    </body>
    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <title>Результаты</title>
    </head>
    <body>
    <h1>Результаты отбора</h1>
    <h2>Претендента на участие в миссии {nickname};</h2>
    <div class="p-3 mb-2 alert-success" style="font-size: 30px">Поздравляем ваш рейтинг после {level} этапа отбора</div>
    <div class="p-3 mb-2 alert-info" style="font-size: 30px">составляет {rating}!</div>
    <div class="p-3 mb-2 alert-warning" style="font-size: 30px">Желаем удачи</div>
    </body>
    </html>'''


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'POST':
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename != '':
                ext = photo.filename.rsplit('.', 1)[1].lower() if '.' in photo.filename else 'png'
                filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext}"
                file_path = os.path.join('static', 'img', filename)
                photo.save(file_path)

                session['photo_path'] = f"img/{filename}"

    photo_path = session.get('photo_path', 'img/photo.png')

    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Загрузка фото</title>
                          </head>
                          <body>
                            <form method="post" enctype="multipart/form-data">
                                <div class="mb-3">
                                    <label for="photo" class="form-label">Загрузка фотографии для участия в миссии</label>
                                    <input type="file" class="form-control" id="photo" name="photo" accept="image/*" required>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                            <div class="mt-3">
                                <img src="{url_for('static', filename=photo_path)}" alt="Ваше фото" class="img-thumbnail" style="max-width: 300px;">
                            </div>
                          </body>
                        </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <title>Карусель</title>
</head>
<body>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img class="d-block w-100" src="https://cool.klev.club/uploads/posts/2025-05/1891/thumbs/matematika_32_7a349719.jpg" alt="First slide">
            </div>
            <div class="carousel-item">
                <img class="d-block w-100" src="https://cool.klev.club/uploads/posts/2025-05/1891/matematika_35_6e570859.jpg" alt="Second slide">
            </div>
            <div class="carousel-item">
                <img class="d-block w-100" src="https://cool.klev.club/uploads/posts/2025-05/1891/thumbs/matematika_45_310c24c7.jpg" alt="Third slide">
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
</body>
</html>'''

if __name__ == '__main__':
    app.secret_key = 'secret-to-make-sessions-work'
    app.run(host='0.0.0.0', port=8080)
