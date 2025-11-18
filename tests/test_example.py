from src.scraper.example_scraper import ExampleScraper

def test_example_scrape_smoke():
    s = ExampleScraper()
    data = s.scrape()
    # It's allowed that network could be blocked in CI; ensure method runs and returns a list
    assert isinstance(data, list)
