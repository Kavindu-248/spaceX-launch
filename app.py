from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return[]

# def catergorize_launches(launches):
#         successful = filter(launches


launches = fetch_spacex_launches()



if __name__ == '__main__':
    app.run(debug=True)

