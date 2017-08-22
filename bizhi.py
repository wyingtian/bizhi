from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world(name="lala"):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
