from bs4 import BeautifulSoup
import requests
from datetime import date, datetime

def get_events(limit_date=None):
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")

    def scrape():
        site_link = 'https://reskilll.com/allevents'
        data = requests.get(site_link)
        return BeautifulSoup(data.text, "html.parser")
    
    page = scrape()

    events_listed = []
    try:
        events = page.find_all(class_="eventtopic eventName pb-2 text-decoration-none")
        for text in events:
            events_listed.append(text.get_text().strip())

    except:
        return []
    
    events_dates_listed = []
    try:
        events = page.find_all(class_="eventdate ps-4")
        for text in events:
            events_dates_listed.append(text.get_text().strip())
    except:
        return []
    
    month_list_num = ['01', '02', '03','04','05','06','07','08','09','10', '11','12']
    month_list = ['Jan', 'Feb', 'Mar', 'Apr',' May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    formatted_dates = []
    for date_str in events_dates_listed:
        date_str = date_str.replace('\n', '').replace('\r', '').replace('\t', '').strip().replace('  ', '-')
        month = date_str[0:3]
        for i,m in enumerate(month_list):
            if month == m:
                date_num = date_str.replace(month, month_list_num[i])
                formatted_date = f"{date_num[-4:]}-{date_num[:5]}"
                formatted_dates.append(formatted_date)
                break

    events_link = []
    try:
        links = page.find_all('a', class_="text-decoration-none registerevent")
        for link in links:
            events_link.append(link['href'])

    except:
        return []

    live_events = []
    today_str = date.today().strftime('%Y-%m-%d')

    for name, event_date, link in zip(events_listed, formatted_dates, events_link):
        if event_date >= today_str:
            if limit_date:
                try:
                    event_date_obj = datetime.strptime(event_date, '%Y-%m-%d').date()
                    if event_date_obj<=limit_date:
                        live_events.append({
                            'name': name,
                            'date': event_date,
                            'link': link
                        })
                except:
                    continue
            else:
                live_events.append({
                    'name':name,
                    'date': event_date,
                    'link': link
                })
    return live_events
