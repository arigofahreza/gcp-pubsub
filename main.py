from src.services.publish import Publisher
from src.services.subscribe import Subscriber

if __name__ == '__main__':
    # Start Publisher
    publisher = Publisher()
    publisher.publish()

    # Start Subscriber
    subscriber = Subscriber()
    subscriber.subscribe()
