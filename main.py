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


@app.route('/image_mars')
def image_mars():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<title>Привет, Марс!</title>
</head>
<body>
<h1>Жди нас, Марс!</h1>
<img src="{url_for('static', filename='img/img.png')}"/>
<p>Марс - красный блин</p>
<div class="p-3 mb-2 bg-primary" style="font-size: 30px">Человечество вырастает из дества</div>
<div class="p-3 mb-2 bg-success" style="font-size: 30px">Человечеству мала одна планета</div>
</body>
</html>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
