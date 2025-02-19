import unittest
from user_util import UserUtil

class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(len(user_id) == 9)
        self.assertTrue(user_id[:2].isdigit())
        self.assertTrue(user_id[2:].isdigit())

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_validate_email(self):
        valid_email = UserUtil.validate_email("adil.toktosunov@example.com")
        invalid_email = UserUtil.validate_email("adil.t@.com")
        self.assertTrue(valid_email)
        self.assertFalse(invalid_email)

    def test_generate_email(self):
        email = UserUtil.generate_email("Adil", "Toktosunov", "example.com")
        self.assertEqual(email, "adil.toktosunov@example.com")

if __name__ == '__main__':
    unittest.main()