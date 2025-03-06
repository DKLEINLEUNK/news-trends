"""
Maintains an in-memory cache of seen articles. 

This module should provide functions for: 
- checking if an article exists; and 
- updating the cache.
"""


class CacheManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager  # BOMBACLAT : New trix just dropped -- Dependency injection of DBManager
        self.cache = self._load_cache()

    def _load_cache(self):
        """Load article titles from the database into an in-memory cache (a set)."""
        # TODO : Only keep the first titles of every news outlet
        return self.db_manager.fetch_titles()

    def store_article(self, article_data):
        """
        Check if an article is new using its title.
        If new, store it in the database and update the cache.
        """
        title = article_data['title']
        if title not in self.cache:
            stored = self.db_manager.store_article(
                title,
                article_data['link'],
                article_data.get('published', '')
            )
            if stored:
                self.cache.add(title)
                return True
        return False
