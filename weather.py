import requests
from bs4 import BeautifulSoup
def scrapeit():
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W8Xep99fgUQ")
    soup = BeautifulSoup(page.content,"html.parser")
    #print(soup.prettify())
    #print(list(soup.children))
    div=soup.find_all('div',id="seven-day-forecast-container")
    seven_day = list(div)[0]
    #print(list(div)[0])

    li = seven_day.find_all('li',class_="forecast-tombstone")
    tombstone = list(li)[0]
    p = tombstone.find_all('p',class_="temp temp-high")
    today = list(p)[0]

    print(today.get_text())
   
scrapeit()
