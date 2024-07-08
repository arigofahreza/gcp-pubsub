from google.cloud import pubsub_v1

from src.configs.pubsub import subscriber_client


class Subscriber:
    def __init__(self):
        self._client, self._subs_path = subscriber_client()

    @staticmethod
    def callback(message) -> None:
        data = message.data.decode('utf-8')
        print(data)
        message.ack()

    def subscribe(self):
        streaming_pull_future = self._client.subscribe(self._subs_path, callback=self.callback)
        with self._client:
            try:
                streaming_pull_future.result(timeout=60)
            except TimeoutError:
                streaming_pull_future.cancel()
                streaming_pull_future.done()
