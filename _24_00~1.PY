
from flask import Flask, render_template
import random
import datetime as dt

          # .now() Method gets the current date and time (very very accurately)

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    this_year = dt.datetime.now().year  # because it is (datetime Module, then datetime Class), to distinguish them from each other, we will rename the datetime Module as 'dt' or datetimeClass
    MY_NAME = "Gavin"
    return render_template('index_server_NWY_D57_v00_r02.html', greeting_string='Hello Jinja!', num=random_number, CURRENT_YEAR=f'Copyright {this_year} - Built by {MY_NAME}')

if __name__ == "__main__":
    app.run(debug=True)