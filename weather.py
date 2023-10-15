import requests
from bs4 import BeautifulSoup

# Function to fetch page content with error handling
def get_page_content(url):
    try:
        page = requests.get(url)
        page.raise_for_status()  # Raise HTTPError for bad responses
        return page.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page content: {e}")
        return None

# Function to get weather information for a city
def get_weather(city, lat, lon):
    # Construct URL for the city
    url = f"https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}"
    
    # Fetch page content
    page_content = get_page_content(url)

    # If page content is available, parse and print weather info
    if page_content is not None:
        soup = BeautifulSoup(page_content, "html.parser")
        div = soup.find_all('div', id="seven-day-forecast-container")
        seven_day = list(div)[0]
        li = seven_day.find_all('li', class_="forecast-tombstone")
        tombstone = list(li)[0]
        p = tombstone.find_all('p', class_="short-desc")
        today = list(p)[0]
        print(f"\t{city}: {today.get_text()}")
    else:
        print(f"Failed to retrieve data for {city}. Please check your internet connection.")

# Functions to get weather for different cities
def scrapeit():
    get_weather("San Francisco", 37.7772, -122.4168)

def scrapeit2():
    get_weather("Apple Valley", 34.5232, -117.2157)

def scrapeit3():
    get_weather("Mojave", 35.1289, -117.9856)

def scrapeit4():
    get_weather("New York", 40.7146, -74.0071)

def scrapeit5():
    get_weather("Los Angeles", 34.0535, -118.2453)

def scrapeit6():
    get_weather("Massachusetts", 42.3657, -71.1083)

def scrapeit7():
    get_weather("California City", 35.1289, -117.9856)

def scrapeit8():
    get_weather("Chicago", 41.8843, -87.6324)

def scrapeit9():
    get_weather("Philadelphia", 38.8182, -76.1587)

def scrapeit10():
    get_weather("Houston", 29.7608, -95.3695)

def scrapeit11():
    get_weather("Miami", 25.7748, -80.1977)

def scrapeit12():
    get_weather("Detroit", 42.3317, -83.048)

# Main execution block
if __name__ == "__main__":
    print("\nWeather conditions later today at :\n")
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
    print("HOUSTON: ")
    scrapeit10()
    print("MIAMI: ")
    scrapeit11()
    print("DETROIT: ")
    scrapeit12()
