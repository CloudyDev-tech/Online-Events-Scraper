from bs4 import BeautifulSoup
import requests

def scrape():

    site_link = "https://devfolio.co/hackathons"

    data = requests.get(site_link)
    data = BeautifulSoup(data.text, "html.parser")
    return data

page=scrape()


events_listed_open = []
# BeautifulSoup.select('h3.sc-dkzDqf lecwTx').text.strip()

try:
    events = page.find_all('a',class_="Link__LinkBase-sc-af40de1d-0 lkflLS")
    for text in events:
        get_event_open = text.get_text()
        print(get_event_open)
        events_listed_open.append(get_event_open)
except:
    message = f"not found !"
    print(message)

print(events_listed_open)


events_link = []
try:
    events = page.find_all('a', class_="Link__LinkBase-sc-af40de1d-0 lkflLS")    
    
    Counter=0
    for ev in events:
        #print(ev.get('href'))
        events_link.append(ev.get('href'))
        Counter+=1
except:
    message = f"not found !"
    print(message)
print(events_link)


events_live_or_ended = []
try:
    # events_term = page.find_all(class_="sc-dkzDqf cqgLqK")    
    c = page.find_all('div', class_ = 'sc-hKMtZM CCkVy')
    for d in c:
        text=d.findNext('p').contents[0]
        print(text)
    #print(c)
    # Counter=0
    # for term in events_term:
    #     get_event_term = term.get_text()
    #     print(get_event_term)
    #     events_live_or_ended.append(get_event_term)
    #     Counter+=1
except:
    message = f"not found !"
    print(message)
print(Counter)
print(events_live_or_ended)