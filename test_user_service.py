import unittest
from datetime import datetime
from user import User
from user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user1 = User(1, "John", "Doe", datetime(1990, 1, 1))
        self.user2 = User(2, "Jane", "Doe", datetime(1995, 5, 15))
        UserService.add_user(self.user1)
        UserService.add_user(self.user2)

    def tearDown(self):
        UserService.delete_user(1)
        UserService.delete_user(2)

    def test_add_user(self):
        self.assertEqual(UserService.get_number(), 2)

    def test_find_user(self):
        found_user = UserService.find_user(1)
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.name, "John")

    def test_delete_user(self):
        UserService.delete_user(1)
        self.assertIsNone(UserService.find_user(1))
        self.assertEqual(UserService.get_number(), 1)

    def test_update_user(self):
        updated_user = User(1, "John", "Smith", datetime(1990, 1, 1))
        UserService.update_user(1, updated_user)
        self.assertEqual(UserService.find_user(1).surname, "Smith")

if __name__ == '__main__':
    unittest.main()