import unittest
from web_interface import app

class TestWebInterface(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Temperatura Atual', response.data)

if __name__ == '__main__':
    unittest.main()