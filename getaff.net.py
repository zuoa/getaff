from flask import Flask,render_template
from flask.ext.login import LoginManager

app = Flask(__name__)
app.debug = True

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/new')
def new():
    return render_template("new.html")

if __name__ == '__main__':
    app.run(port=2345)
