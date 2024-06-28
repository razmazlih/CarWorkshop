from flask import Flask, render_template
from cars.menu import car_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(car_blueprint, url_prefix='/cars')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)