import mysql.connector

def stream_users():
    conect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='ALX_prodev'

    )
    currsor = conect.cursor()
    sql = 'SELECT * FROM user_data'
    currsor.execute(sql)
    for row in currsor:
        yield row

    