import json
import feedparser


def load_urls(file, region="NL"):
    """Load URLs from a JSON file."""
    with open(file, 'r') as f:
        data = json.load(f)
    return data.get(region, [])