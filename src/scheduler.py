"""Simple scheduler using APScheduler to run the example scraper periodically."""
import os
import json
from apscheduler.schedulers.blocking import BlockingScheduler
from src.scraper.example_scraper import ExampleScraper

scheduler = BlockingScheduler()

def job_example():
    print('Running scheduled example scraper...')
    s = ExampleScraper()
    data = s.scrape()
    os.makedirs('data', exist_ok=True)
    out = os.path.join('data', 'scheduled_output.json')
    with open(out, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=2)
    print(f'Saved {len(data)} records to {out}')

if __name__ == '__main__':
    scheduler.add_job(job_example, 'interval', minutes=30, id='example_job')
    print('Starting scheduler (Ctrl+C to exit)...')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print('Scheduler stopped.')
