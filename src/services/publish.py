import json
import uuid

from src.configs.pubsub import publisher_client
from faker import Faker


class Publisher:
    def __init__(self):
        self._client, self._topic_path = publisher_client()
        self._fake = Faker()

    def publish(self):
        for index in range(1000):
            student_data = {
                'id': str(uuid.uuid4()),
                'name': self._fake.name(),
                'address': self._fake.address(),
                'latitude': str(self._fake.latitude()),
                'longitude': str(self._fake.longitude())
            }
            str_student_data = json.dumps(student_data)
            encoded_student_data = str_student_data.encode('utf-8')
            future = self._client.publish(self._topic_path, encoded_student_data)
            print(future.result())
