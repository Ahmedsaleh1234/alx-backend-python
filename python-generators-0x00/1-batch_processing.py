import mysql.connector
def stream_users_in_batches(batch_size):
    connect = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='ALX_prodev'
    )
    cursor = connect.cursor()
    sql = 'SELECT * FROM user_data'
    cursor.execute(sql)
    
    batch = []
    for _ in range(batch_size):
        row = cursor.fetchone()
        if not row:
            break
        batch.append(row)
    yield batch
def batch_processing(batch_size):
    for  batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user[3] > 25:
                print(user)


