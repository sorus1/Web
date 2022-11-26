from flask import Flask
from flask import url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    user = "Руслан"
    return render_template("index.html", title="Домашняя страница", username=user)

@app.route("/gis")
def gis():
    user = "Руслан"
    return render_template("gis.html", title="Домашняя страница", username=user)


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/111.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''

@app.route('/sample_page')
def return_sample_page():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Колледж!</title>
                      </head>
                      <body>
                        <h1>Привет, Колледж!</h1>
                        <div class="alert alert-primary" role="alert">
                          А мы тут компонентами Bootstrap балуемся
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')