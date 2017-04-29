from flask import Flask, render_template

from utils.math_views import math_views

app = Flask(__name__)
app.register_blueprint(math_views)

@app.route('/')
def home():
    return render_template('index.html')


def main():
    app.debug = True
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
