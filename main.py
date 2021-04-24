from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def ad():
    ad_text = ["Человечество вырастает из детства.",
               "Человечеству мала одна планета.",
               "Мы сделаем обитаемыми безжизненные пока планеты.",
               "И начнем с Марса!",
               "Присоединяйся!"]
    return '</br></br>'.join(ad_text)


@app.route('/image_mars')
def mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}">
                        <div class="alert alert-dark" role="alert">
                            <h2>Человечество вырастает из детства.</h2>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <h2>Человечеству мала одна планета.</h2>
                        </div>
                        <div class="alert alert-dark" role="alert">
                            <h2>Мы сделаем обитаемыми безжизненные пока планеты.</h2>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <h2>И начнем с Марса!</h2>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <h2>Присоединяйся!</h2>
                        </div>
                      </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for("static", filename="css/style.css")}">
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div class="top_text">
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                    <div class="name_and_surname_input">
                                        <input type="surname" class="form-control" placeholder="Введите фамилию" name="surname">
                                        <input type="name" class="form-control" placeholder="Введите имя" name="name">
                                    </div>
                                    <div class="email_input">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </div>
                                    <div class="education_level_input">
                                        <label for="educationSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="profession">
                                        <label>Какие у вас есть профессии?</label>
                                        <p><input type="checkbox" name="a" value="Инженер-исследователь">Инженер-исследователь</p>
                                        <p><input type="checkbox" name="a" value="Инженер-строитель">Инженер-строитель</p>
                                        <p><input type="checkbox" name="a" value="Пилот">Пилот</p>
                                        <p><input type="checkbox" name="a" value="Метеоролог">Метеоролог</p>
                                        <p><input type="checkbox" name="a" value="Инженер по жизнеобеспечению">Инженер по жизнеобеспечению</p>
                                        <p><input type="checkbox" name="a" value="Инженер по радиационной защите">Инженер по радиационной защите</p>
                                        <p><input type="checkbox" name="a" value="Врач">Врач</p>
                                        <p><input type="checkbox" name="a" value="Экзобиолог">Экзобиолог</p>
                                    </div>
                                    <div class="sex_choice">
                                        <label>Укажите пол</label>
                                        <p><input type="radio" name="sex" value="male">Мужской</p>
                                        <p><input type="radio" name="sex" value="female">Женский</p>
                                    </div>
                                    <div class="motivation">
                                        <label for="about">Почему Вы хотите принять участие в мисии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="photo">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="accept">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet_name};</h1>
                        <h2>Эта планета близка к Земле;</h2>
                        <div class="alert alert-success" role="alert">
                            <h2>На ней много необходимых ресурсов;</h2>
                        </div>
                        <div class="alert alert-dark" role="alert">
                            <h2>На ней есть вода и атмосфера;</h2>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <h2>На ней есть небольшое магнитное поле;</h2>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <h2>Наконец, она просто красива!</h2>
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в мисси {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                        <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                    </div>
                    <h3>составляет {rating}</h3>
                    <div class="alert alert-warning" role="alert">
                        <h2>Желаем удачи!</h2>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
