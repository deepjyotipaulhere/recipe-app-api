from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successfull"""
        email = 'test@google.com'
        password = 'Testpass@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests if new user email is normalized"""
        email = 'test@GooGle.com'
        user = get_user_model().objects.create_user(email, 'test@123')

        self.assertEqual(user.email, user.email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '332')

    # def test_create_new_superuser(self):
    #     """Test creating a new super user"""
    #     user = get_user_model().objects.create_superuser(
    # 'test@gmail.com', 'pass@123')
    #     self.assertTrue(user.is_superuser)
    #     self.assertTrue(user.is_staff)
