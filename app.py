from flask import Flask, render_template, request
from events_scraper import get_events
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/reskilll', methods=['GET', 'POST'])
def reskilll():
    limit_date=None
    if request.method == 'POST':
        limit_date_dtr =  request.form.get('limit_date')
        if limit_date_dtr:
            try:
                limit_date = datetime.strptime(limit_date_dtr, '%Y-%m-%d').date()
            except ValueError:
                limit_date = None
    
    events = get_events(limit_date=limit_date)
    current_date = datetime.now().strftime('%Y-%m-%d')

    return render_template('reskilll.html', events=events, limit_date=limit_date, current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True)
