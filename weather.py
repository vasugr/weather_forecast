import json
import requests
from bs4 import BeautifulSoup
from pylsy import pylsytable

def load_cities(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

class WeatherScraper:
    def __init__(self, cities_file):
        self.cities = load_cities(cities_file)

    def _get_page_content(self, url):
        try:
            page = requests.get(url)
            page.raise_for_status()
            return page.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page content: {e}")
            return None

    def _extract_weather_from_page(self, page_content):
        if not page_content:
            return None
        soup = BeautifulSoup(page_content, "html.parser")
        div = soup.find('div', id="seven-day-forecast-container")
        if not div:
            return None
        li = div.find('li', class_="forecast-tombstone")
        if not li:
            return None
        p = li.find('p', class_="short-desc")
        if not p:
            return None
        return p.get_text()

    def _extract_cloud(self, page_content):
        if not page_content:
            return None
        soup = BeautifulSoup(page_content, "html.parser")
        div = soup.find('div', id="current_conditions-summary")
        if not div:
            return None
        p = div.find('p', class_="myforecast-current")
        if not p:
            return None
        return p.get_text()

    def _extract_temp_F(self, page_content):
        if not page_content:
            return None
        soup = BeautifulSoup(page_content, "html.parser")
        div = soup.find('div', id="current_conditions-summary")
        if not div:
            return None
        p = div.find('p', class_="myforecast-current-lrg")
        if not p:
            return None
        return p.get_text()
    
    def _extract_temp_C(self, page_content):
        if not page_content:
            return None
        soup = BeautifulSoup(page_content, "html.parser")
        div = soup.find('div', id="current_conditions-summary")
        if not div:
            return None
        p = div.find('p', class_="myforecast-current-sm")
        if not p:
            return None
        return p.get_text()

    def _get_weather(self, city, lat, lon):
        url = f"https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}"
        page_content = self._get_page_content(url)
        weather = self._extract_weather_from_page(page_content)
        cloud = self._extract_cloud(page_content)
        temp_F = self._extract_temp_F(page_content)
        temp_C = self._extract_temp_C(page_content)

        data = []

        # Error checking for each attribute
        if weather:
            data.append(weather)
        else:
            data.append("Unable to retrieve weather.")

        if cloud:
            data.append(cloud)
        else:
            data.append("Unable to retrieve cloud.")

        if temp_F:
            data.append(temp_F)
        else:
            data.append("Unable to retrieve temp (F).")

        if cloud:
            data.append(temp_C)
        else:
            data.append("Unable to retrieve temp (C).")

        return data



    def scrape_all_weather(self):

        # Initiate pylsy table with desired attributes
        attrs = ["LOCATION", "FORECAST", "CLOUD", "TEMP-F", "TEMP-C"]
        table = pylsytable(attrs)

        # Create lists to store data of each attribute
        locations = []
        forecasts = []
        clouds = []
        tempsF = []
        tempsC = []

        print("\nWeather conditions later today:\n")
        for city, coords in self.cities.items():
            locations.append(city)
            weather_info = self._get_weather(city, coords['lat'], coords['lon'])

            # Store weather_info in two separate lists to feed into pylsy
            forecasts.append(weather_info[0])
            clouds.append(weather_info[1])
            tempsF.append(weather_info[2])
            tempsC.append(weather_info[3])

        # Feed data into pylsy table
        table.add_data("LOCATION", locations)
        table.add_data("FORECAST", forecasts)
        table.add_data("CLOUD", clouds)
        table.add_data("TEMP-F", tempsF)
        table.add_data("TEMP-C", tempsC)
        
        print(table)


if __name__ == "__main__":
    scraper = WeatherScraper('cities.json')
    scraper.scrape_all_weather()

