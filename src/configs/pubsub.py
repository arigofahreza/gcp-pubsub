from pydantic_settings import BaseSettings
from google.cloud import pubsub_v1


class PubsubConfig(BaseSettings):
    PROJECT_ID: str
    TOPIC_ID: str
    SUBSCRIPTION_ID: str

    class Config:
        env_file = ".env"


def publisher_client():
    config = PubsubConfig()
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(config.PROJECT_ID, config.TOPIC_ID)
    return publisher, topic_path


def subscriber_client():
    config = PubsubConfig()
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(config.PROJECT_ID, config.SUBSCRIPTION_ID)
    return subscriber, subscription_path
