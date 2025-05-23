from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Coucou !"

@app.route('/cart')
def cart():
    return "Parnier vide !"

if __name__ == '__main__':
    app.run(debug=True)