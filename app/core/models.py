from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields): # **extra_fields means unwind *args **kwargs
		if not email:
			raise ValueError("Users must have a email address")

		# Create and save a new user
		# https://stackoverflow.com/a/64456227, use - email=email or else ValueError: Field 'id' expected a number but got 'test@example.com'.
		# self.normalize_email - is a helper function that comes with BaseUserManager
		user = self.model(email=self.normalize_email(email), **extra_fields) # Not sure where .model is coming from
		user.set_password(password)
		user.save(using=self._db) # This syntax is for using multiple DB's but we won't be doing that in this course

		return user

	# Create super - user is a built in Django function that is used to create superusers with the command line
	def create_superuser(self, email, password):
		# Create and save new super user
		# **extra_fields is not necessary becuase we are creating the superuser with the cmd line

		user = self.create_user(email=email, password=password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db) # This syntax is for using multiple DB's but we won't be doing that in this course

		return user

		

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False) 

	objects = UserManager()

	USERNAME_FIELD = "email"
