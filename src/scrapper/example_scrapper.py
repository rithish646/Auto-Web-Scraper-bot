"""Example scraper that scrapes http://quotes.toscrape.com/ for demo purposes."""
import requests
from bs4 import BeautifulSoup
from .base import BaseScraper

class ExampleScraper(BaseScraper):
    BASE_URL = 'http://quotes.toscrape.com'

    def scrape(self):
        results = []
        page = 1
        while True:
            url = f"{self.BASE_URL}/page/{page}/"
            try:
                resp = requests.get(url, timeout=10)
            except Exception:
                break
            if resp.status_code != 200:
                break
            soup = BeautifulSoup(resp.text, 'html.parser')
            quotes = soup.select('div.quote')
            if not quotes:
                break
            for q in quotes:
                text = q.select_one('span.text').get_text(strip=True)
                author = q.select_one('small.author').get_text(strip=True)
                tags = [t.get_text(strip=True) for t in q.select('div.tags a.tag')]
                results.append({'text': text, 'author': author, 'tags': tags})
            page += 1
        return results
