from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase): 

	def test_create_user_with_email_successful(self):
		# Test creating new user with email
		email = "test@example.com"
		password = 'test1234'
		user = get_user_model().objects.create_user(
			email=email,
			password=password
		)


		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	def test_new_user_email_normalized(self):
		# Test the email for a new user is normalized
		email = "test@LONDONAPP.COM"
		user = get_user_model().objects.create_user(
			email=email, 
			password="test1234"
		)
		
		self.assertEqual(user.email, email.lower())

	def test_new_user_invalid_email(self):
		# Test creating new user with no email raises error
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(email=None, password="test1234")


	def test_create_new_superuser(self):

		user = get_user_model().objects.create_user(
                        email="test@londonappdev.com", 
                        password="test1234",
			is_superuser=True,
			is_staff=True
                )

		# Test creating new superuser
		self.assertTrue(user.is_superuser) # is_superuser - is built into the PermissionsMixin in models.py
		self.assertTrue(user.is_staff)
