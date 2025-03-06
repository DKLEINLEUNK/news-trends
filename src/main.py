import feedparser

from database.db_manager import DBManager
from cache.cache_manager import CacheManager
from utils import load_urls
from rss.fetcher import fetch_rss


def main():

    # 1. Initialize the database & co
    db_manager = DBManager()
    cache_manager = CacheManager(db_manager)  # get injected nerd

    # 2. Fetch the urls
    urls = load_urls("rss-feeds.json")
    for url in urls:

        # 2.1. Fetch news entries from url
        entries = fetch_rss(url)
        for entry in entries:

            # 2.2. Store entries in db (if not in cache)
            if cache_manager.store_article(entry):
                print("[db_manager]: Stored new article by %s" % (entry["source"]))

    # 3. Close up the db like a good little slut
    db_manager.close_connection()


if __name__ == "__main__":
    main()