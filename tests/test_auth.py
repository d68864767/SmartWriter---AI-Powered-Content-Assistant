```python
import unittest
from auth import hash_password, verify_password, save_user, authenticate_user

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        save_user(self.username, self.password)

    def test_hash_password(self):
        hashed_password = hash_password(self.password)
        self.assertEqual(len(hashed_password), 128)

    def test_verify_password(self):
        hashed_password = hash_password(self.password)
        self.assertTrue(verify_password(hashed_password, self.password))

    def test_save_user(self):
        new_username = "newuser"
        new_password = "newpassword"
        save_user(new_username, new_password)
        self.assertTrue(authenticate_user(new_username, new_password))

    def test_authenticate_user(self):
        self.assertTrue(authenticate_user(self.username, self.password))
        self.assertFalse(authenticate_user(self.username, "wrongpassword"))
        self.assertFalse(authenticate_user("wronguser", self.password))

if __name__ == '__main__':
    unittest.main()
```
