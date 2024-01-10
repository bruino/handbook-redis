import time
import json
from faker import Faker
import redis

fake = Faker()
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def generate_sensor_data():
    sensor_data = {
        'timestamp': int(time.time()),
        'sensor_id': fake.uuid4(),
        'temperature': fake.random_int(10, 30),
        'humidity': fake.random_int(30, 70),
    }
    return json.dumps(sensor_data)

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        redis_client.publish('sensor_data_channel', data)
        print(f"Data sent: {data}")
        time.sleep(1)