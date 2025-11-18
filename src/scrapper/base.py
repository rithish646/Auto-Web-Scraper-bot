from typing import List, Dict

class BaseScraper:
    """Small base class all scrapers should extend."""
    def __init__(self, **kwargs):
        self.config = kwargs

    def scrape(self) -> List[Dict]:
        """Perform scraping and return list of dicts."""
        raise NotImplementedError("scrape must be implemented by subclasses")
