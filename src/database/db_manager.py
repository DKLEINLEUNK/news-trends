"""Serious swag alert rn, ngl"""

import sqlite3


class DBManager:
    def __init__(self, db_path='news.db'):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self._init_db()
    
    def _init_db(self):
        c = self.connection.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE,
                link TEXT,
                published TEXT
            )
        ''')
        self.connection.commit()
    
    def get_connection(self):
        return self.connection

    def store_article(self, title, link, published):
        c = self.connection.cursor()
        try:
            c.execute("INSERT INTO articles (title, link, published) VALUES (?, ?, ?)", (title, link, published))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def fetch_titles(self):
        c = self.connection.cursor()
        c.execute("SELECT title FROM articles")
        rows = c.fetchall()
        return {row[0] for row in rows}

    def query_db(self, query, params=None):
        """
        Execute an arbitrary SQL query and return the results.
        
        :param query: A valid SQL query string.
        :param params: A tuple/list of parameters to safely bind to the query.
        :return: A list of tuples containing the result set.
        """
        if params is None:
            params = ()
        c = self.connection.cursor()
        c.execute(query, params)
        results = c.fetchall()
        return results

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None


if __name__ == "__main__":
    # Instantiate the DBManager
    db_manager = DBManager('news.db')

    # Example 1: Query all articles
    all_articles = db_manager.query_db("SELECT * FROM articles")
    print(all_articles)

    # # Example 2: Query articles with a specific id
    # id_to_find = 1
    # results = db_manager.query_db("SELECT * FROM articles WHERE id = ?", (id_to_find,))
    # print(results)

    db_manager.close_connection()
