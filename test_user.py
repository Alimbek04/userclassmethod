import unittest
from datetime import datetime
from user import User

class TestUser (unittest.TestCase):
    def test_user_creation(self):
        user = User(1, "John", "Doe", datetime(1990, 1, 1))
        self.assertEqual(user.get_details(), "User   ID: 1, Name: John Doe, Email: None, Birthday: 1990-01-01")
        self.assertEqual(user.get_age(), datetime.now().year - 1990)

    def test_user_age(self):
        user = User(2, "Jane", "Doe", datetime(2000, 1, 1))
        self.assertEqual(user.get_age(), datetime.now().year - 2000)

if __name__ == '__main__':
    unittest.main()