"""Retrieves and parses the RSS feeds."""

import feedparser


def fetch_rss(url):
  """Fetches RSS feed from the provided url

  Args:
    url (str): The URL to the RSS feed.

  Return:
    entries (list): List of fetched articles as dictionaries.
  """
  d = feedparser.parse(url)
  entries = []
  for entry in d.entries:
    article = {
      "source": d.feed.title,
      "title": entry.title,
      "link": entry.link,
      "published": entry.get("published", "")
    }
    entries.append(article)
  return entries