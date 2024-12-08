import sqlite3
from datetime import datetime
def log_queries(func):
    """
    decorator log the sql query
    """
    def wrapper(*args, **kwargs):
        startTime = datetime.now()
        query = kwargs.get('query') or args[0]
        print(f'exexuting query {query}')
        endTime = datetime.now()
        return func(*args, **kwargs)
    return wrapper
    
    
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
users = fetch_all_users(query='SELECT * FROM users')
print(users)