import unittest
from datetime import datetime
from user import User

class TestUser (unittest.TestCase):
    def test_user_creation(self):
        user = User(1, "Adil", "Toktosunov", datetime(2004, 6, 16))
        self.assertEqual(user.get_details(), "User   ID: 1, Name: Adil Toktosunov, Email: None, Birthday: 2004-06-16")
        self.assertEqual(user.get_age(), datetime.now().year - 2004)

    def test_user_age(self):
        user = User(2, "Jane", "T", datetime(2025, 2, 19))
        self.assertEqual(user.get_age(), datetime.now().year - 2025)

if __name__ == '__main__':
    unittest.main()