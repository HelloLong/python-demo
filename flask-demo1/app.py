from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! I am created by pycharm'


if __name__ == '__main__':
    app.run()
