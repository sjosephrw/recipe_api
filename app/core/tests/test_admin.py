from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
	
	# Function to run before running the tests
	def setUp(self):
		self.client = Client()
		self.admin_user = get_user_model().objects.create_superuser(
			email="admin@londonappdev.com",
			password="test1234"
		)

		
		# Automatically login the user
		self.client.force_login(self.admin_user)
		self.user = get_user_model().objects.create_user(
			email="test@londonappdev.com",
			password="test1234"
		)


	def test_users_listed(self):
		# Test that users are listed on user page
		# reverse - if the url is changed in the future we dont need to change it every where
		# admin:core_user_changelist -  built in django admin url
		url = reverse("admin:core_user_changelist")
		res = self.client.get(url)

		# assertContains - also checks for httpStatus 200, and the res object properties
		self.assertContains(res, self.user.name)
		self.assertContains(res, self.user.email)

	def test_user_change_page(self):
		'''Test that the user edit page works'''
		#The reverse function will generate  /admin/core/user/:id - id is supplied into args=[self.user.id]
		url = reverse('admin:core_user_change', args=[self.user.id])
		res = self.client.get(url)

		# If the above  url works then the status code will be 200
		self.assertEqual(res.status_code, 200)


	def test_create_user_page(self):
		# Test that the create user page works
		url = reverse('admin:core_user_add')
		res = self.client.get(url)
                # If the above  url works then the status code will be 200
		self.assertEqual(res.status_code, 200)
