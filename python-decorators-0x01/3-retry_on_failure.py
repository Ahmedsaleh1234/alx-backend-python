import time
import sqlite3 
import functools

#### paste your with_db_decorator here

""" your code goes here"""
def with_db_connection(func):
    """
    handling connection to dbs
    """
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper
def retry_on_failure(retries, delay):
    def wrap(func):
        def wrapper(*args, **kwargs):
            tem = 0
            while(tem < retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tem += 1
                    print(f'atempt number{tem} failed: {e} ')
                    if(tem < retries):
                        time.sleep(delay)
                    else:
                        print('all attemped failed')
        return wrapper
    return wrap


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)