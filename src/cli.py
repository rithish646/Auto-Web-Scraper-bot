"""Simple CLI to run scrapers"""
import argparse
import json
from src.scraper.example_scraper import ExampleScraper

SCRAPERS = {
    "example": ExampleScraper,
}

def main():
    parser = argparse.ArgumentParser(description='Automation & Web Scraper Bot CLI')
    sub = parser.add_subparsers(dest='command')
    run = sub.add_parser('run', help='Run a scraper once')
    run.add_argument('--scraper', required=True, choices=SCRAPERS.keys())
    run.add_argument('--output', required=True, help='Output file (JSON)')

    args = parser.parse_args()
    if args.command == 'run':
        scraper_cls = SCRAPERS[args.scraper]
        scraper = scraper_cls()
        data = scraper.scrape()
        with open(args.output, 'w', encoding='utf-8') as fh:
            json.dump(data, fh, indent=2)
        print(f"Saved {len(data)} records to {args.output}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
