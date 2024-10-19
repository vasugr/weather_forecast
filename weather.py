import json
import requests
from bs4 import BeautifulSoup

class WeatherScraper:
    def __init__(self, cities_file):
        self.cities = self.load_cities(cities_file)

    def load_cities(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def _get_page_content(self, url):
        try:
            page = requests.get(url)
            page.raise_for_status()
            return page.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page content: {e}")
            return None
            
    def _extract_weather_from_page(self, page_content):
        if page_content:
            soup = BeautifulSoup(page_content, "html.parser")
            div = soup.find('div', id="seven-day-forecast-container")
            if div:
                li = div.find('li', class_="forecast-tombstone")
                if li:
                    p = li.find('p', class_="short-desc")
                    if p:
                        return f"\t{city}: {p.get_text()}"
        return None

    def get_weather(self, city, lat, lon):
        url = f"https://forecast.weather.gov/MapClick.php?lat={lat}&lon={lon}"
        page_content = self._get_page_content(url)
        return self._extract_weather_from_page(page_conetnt)
        
        return f"Failed to retrieve data for {city}. Please check your internet connection."

    def scrape_all_weather(self):
        print("\nWeather conditions later today:\n")
        for city, coords in self.cities.items():
            print(f"{city.upper()}: ")
            print(self.get_weather(city, coords['lat'], coords['lon']))

if __name__ == "__main__":
    scraper = WeatherScraper('cities.json')
    scraper.scrape_all_weather()
