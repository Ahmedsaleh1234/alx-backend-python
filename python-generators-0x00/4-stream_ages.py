seed = __import__('seed')
def stream_user_ages():
    connect = seed.connect_to_prodev()
    cursor = connect.cursor(dictionary=True)
    sql = "SELECT age FROM user_data"
    cursor.execute(sql)
    for row in cursor:
        yield row['age']

def calulate_age():
    count = 0
    total_age = 0
    for age in stream_user_ages():
        count += 1
        total_age += age
    average = total_age / count
    print(f'the average = {average}') 
calulate_age()