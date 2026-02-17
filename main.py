from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Миссия Колонизация Марса'

@app.route('/promotion')
def index():
    return '''Человечество вырастает из детства.

Человечеству мала одна планета.

Мы сделаем обитаемыми безжизненные пока планеты.

И начнем с Марса!

Присоединяйся!'''


@app.route('/image_mars')
def index():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Привет, Марс!</title>
</head>
<body>
<main>
<h1>Welcome to My Website</h1>
<p>This is a paragraph.</p>
</main>
<script src="index.js"></script>
</body>
</html>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)