from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'It works !'


if __name__ == '-_main_-':
    app.run()
