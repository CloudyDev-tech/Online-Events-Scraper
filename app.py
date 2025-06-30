from flask import Flask, render_template
from events_scraper import get_events
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reskilll')
def reskilll():
    events = get_events()
    return render_template('reskilll.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
