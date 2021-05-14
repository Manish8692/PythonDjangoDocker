from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "sonarmanish9@gmail.com"
        password = "Msonar@8692"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for new user with normalize """
        email = "manish@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "123456")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email falses error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "123456")

    def test_create_new_superuser(self):
        """ Test create new superuser"""
        user = get_user_model().objects.create_superuser(
            'manishsonar@gmail.com',
            'test123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
