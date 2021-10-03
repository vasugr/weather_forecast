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
    p = tombstone.find_all('p',class_="short-desc")
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
    p = tombstone.find_all('p',class_="short-desc")
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
    p = tombstone.find_all('p',class_="short-desc")
    today = list(p)[0]

    print(today.get_text())
    
def scrapeit4():
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.XZNKc3EzYUM")
    soup = BeautifulSoup(page.content,"html.parser")
    #print(soup.prettify())
    #print(list(soup.children))
    div=soup.find_all('div',id="seven-day-forecast-container")
    seven_day = list(div)[0]
    #print(list(div)[0])

    li = seven_day.find_all('li',class_="forecast-tombstone")
    tombstone = list(li)[0]
    p = tombstone.find_all('p',class_="short-desc")
    today = list(p)[0]

    print(today.get_text())

 
def scrapeit5():
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453")
    soup = BeautifulSoup(page.content,"html.parser")
    div=soup.find_all('div',id="seven-day-forecast-container")
    seven_day = list(div)[0]
    li = seven_day.find_all('li',class_="forecast-tombstone")
    tombstone = list(li)[0]
    p = tombstone.find_all('p',class_="short-desc")
    today = list(p)[0]

    print(today.get_text())
    
def scrapeit6():#For Massachusetts
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.3657&lon=-71.1083#.XZc1T3X7Q-Y")
    soup = BeautifulSoup(page.content,"html.parser")
    div=soup.find_all('div',id="seven-day-forecast-container")
    seven_day = list(div)[0]
    li = seven_day.find_all('li',class_="forecast-tombstone")
    tombstone = list(li)[0]
    p = tombstone.find_all('p',class_="short-desc")
    today = list(p)[0]

    print(today.get_text())
    
def scrapeit7():#For California City
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=35.1289&lon=-117.9856#.XZc4BnX7Q-Y")
    soup = BeautifulSoup(page.content,"html.parser")
    div=soup.find_all('div',id="seven-day-forecast-container")
    seven_day = list(div)[0]
    li = seven_day.find_all('li',class_="forecast-tombstone")
    tombstone = list(li)[0]
    p = tombstone.find_all('p',class_="short-desc")
    today = list(p)[0]

    print(today.get_text())
    
def scrapeit8():#For Chicago
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XZc573X7Q-Y")
    soup = BeautifulSoup(page.content,"html.parser")
    div=soup.find_all('div',id="seven-day-forecast-container")
    seven_day = list(div)[0]
    li = seven_day.find_all('li',class_="forecast-tombstone")
    tombstone = list(li)[0]
    p = tombstone.find_all('p',class_="short-desc")
    today = list(p)[0]

    print(today.get_text())

def scrapeit9():#For pHILADELPHIA
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=38.8182&lon=-76.1587")
    soup = BeautifulSoup(page.content,"html.parser")
    div=soup.find_all('div',id="seven-day-forecast-container")
    seven_day = list(div)[0]
    li = seven_day.find_all('li',class_="forecast-tombstone")
    tombstone = list(li)[0]
    p = tombstone.find_all('p',class_="short-desc")
    today = list(p)[0]

    print(today.get_text())
    
print("\nToday's temperature at :\n")
print("SAN FRANCISCO: ")
scrapeit()
print("APPLE VALLEY: ")
scrapeit2()
print("MOJAVE: ")
scrapeit3()
print("NEW YORK: ")
scrapeit4()
print("LOS ANGELES: ")
scrapeit5()
print("MASSACHUSETTS: ")
scrapeit6()
print("CALIFORNIA CITY: ")
scrapeit7()
print("CHICAGO: ")
scrapeit8()
print("PHILADELPHIA: ")
scrapeit9()