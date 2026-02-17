from flask import Flask, url_for

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
<div class="p-3 mb-2 alert-primary" style="font-size: 30px">Человечество вырастает из дества</div>
<div class="p-3 mb-2 alert-secondary" style="font-size: 30px">Человечеству мала одна планета</div>
<div class="p-3 mb-2 alert-success" style="font-size: 30px">Человечеству мала одна планета</div>
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
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
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
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
