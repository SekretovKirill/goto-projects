from flask import Flask
import random
app = Flask(__name__)
weath = ['солнечно', 'очень солнечно', 'дождь', 'пасмурно', 'град', 'гроза', 'глобальное потепление']
@app.route('/')
def site():
    return '''
    <html>
        <body>
            <h3>Это главная страница сайта</h3>
            <a href=" http://127.0.0.1:8080/weather">Погода</a>
            
                <a href="http://127.0.0.1:8080/me">Личное дело</a>
        </body>
    </html>
    '''

@app.route('/weather')
def weather():
    r = random.randint(1, 7)
    a =weath[r]
    return """
    <html>
        <body>
        прогноз погоды на завтра: завтра будет {a}
        </body>
    </html>
    """.format(a=a)
@app.route('/me')
def me():
    return """
    <html>
        <body>
        <img src='https://how.qip.ru/resize/420/330/w/uploads/articles/c98697536da9a9d46aad8d4b1227c2c0.jpg'>
            <h2>Меня зовут презентабельный_мужчина.jpg и это мой сайт.</h2>
            <b>У меня</b> <s>есть много</s> <h1>интересов.</h1>
             <u>Один из них</u> - <b><s><h1><u>эксперементировать со шрифтами.</b></s></h1></u>
        </body>
    </html>
    """

app.run(debug=True, port=8080)