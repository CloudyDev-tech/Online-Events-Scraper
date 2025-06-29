from bs4 import BeautifulSoup
import requests
from datetime import date

#extracting today's date
today = date.today()
date_str = today.strftime("%Y-%m-%d")
print("Today's date:", date_str)

def scrape():
    site_link = 'https://reskill.com/allevents'

    data = requests.get(site_link)
    data = BeautifulSoup(data.text, "html.parser")
    return data

page = scrape()

events_listed = []
try:
    events = page.find_all(class_="eventtopic eventName pb-2")
    for text in events:
        get_event = text.get_text()

        events_listed.append(get_event)
except:
    message = f"not found !"
    print(message)

# print("Events listed today:", len(events_listed))
# print("Events:", events_listed)

events_name = []
for i in range(len(events_listed)):
    for j in events_listed[i]:
        if j=='\n' or j=='\r' or j=='\t' or j==' ':
            event_name = (events_listed[i].replace(j, "")).strip()
            if event_name:
                events_name.append(event_name)
                break

# print("Events:", events_name)

#EVENT DATES

events_dates_listed = []
try:
    events = page.find_all(class_="eventdate ps-4")
    for text in events:
        get_event = text.get_text()

        events_dates_listed.append(get_event)
except:
    message = f"not found !"
    print(message)

# print("Events dates:", events_dates_listed)
            
month_list_num = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
events_date = []
live_events_date=[]

for i in range(len(events_dates_listed)):
    for j in events_dates_listed[i]:
        if j=='\n' or j=='\r' or j=='\t' or j==' ':
            event_date = (((events_dates_listed[i].replace('\n','')).strip()).replace(' ','-'))
            
            a = event_date[0:3]

            for k in range(len(month_list)):
                if a == month_list[k]:
                    event_dates_num=event_date[0:3].replace(a,month_list_num[k])+event_date[3:]
                    #print(event_dates_num)
            event_date_formatted = event_dates_num[-4:]+'-'+event_dates_num[:5]
            events_date.append(event_date_formatted)
            break 
# print("Events date:", events_date)
#LIVE EVENTS

count_live = 0
for i in range(len(events_date)):
    if events_date[i] >= date_str:
        live_events_date.append(events_date[i])
        count_live += 1
        print(f"{count_live}. {events_name[i]}")
        # print(f"{count_live}. {events_name[i]} on {events_date[i]}")

print(f"\nTotal live events today: {count_live}")

