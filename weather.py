import json
import requests
from bs4 import BeautifulSoup

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

    def _get_weather(self, city, lat, lon):
        url = f"https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}"
        page_content = self._get_page_content(url)
        weather = self._extract_weather_from_page(page_content)
        if weather:
            return f"{city.upper()}: {weather}"
        return f"{city.upper()}: Unable to retrieve data. Please check your internet connection."

    def scrape_all_weather(self):
        print("\nWeather conditions later today:\n")
        for city, coords in self.cities.items():
            weather_info = self._get_weather(city, coords['lat'], coords['lon'])
            print(f"    {weather_info}")

if __name__ == "__main__":
    scraper = WeatherScraper('cities.json')
    scraper.scrape_all_weather()

