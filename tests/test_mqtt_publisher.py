import unittest
from unittest.mock import patch
import paho.mqtt.client as mqtt
from mqtt_publisher import on_connect

class TestMQTTPublisher(unittest.TestCase):
    @patch('mqtt_publisher.mqtt.Client')
    def test_on_connect(self, MockClient):
        client = MockClient.return_value
        on_connect(client, None, None, 0)
        client.connect.assert_called_once_with("broker.hivemq.com", 1883, 60)

if __name__ == '__main__':
    unittest.main()