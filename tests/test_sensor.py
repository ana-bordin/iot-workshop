import unittest
from sensor import read_sensor_data

class TestSensor(unittest.TestCase):
    def test_read_sensor_data(self):
        data = read_sensor_data()
        self.assertTrue(20.0 <= data <= 25.0)

if __name__ == '__main__':
    unittest.main()