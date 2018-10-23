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
   
def scrapeit2():
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.5232&lon=-117.2157#.W89OAo5fgUQ")
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
    
def scrapeit3():
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=35.1289&lon=-117.9856#.W89Q_Y5fgUQ")
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

print("SAN FRANCISCO: ")
scrapeit()
print("APPLE VALLEY: ")
scrapeit2()
print("MOJAVE: ")
scrapeit3()

