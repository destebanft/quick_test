from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts.managers.auth_user_manager import AuthUserManager


class AuthUser(AbstractUser):
	first_name = models.CharField(
		_('fisrt name'),
		blank=True,
		null=True,
		max_length=30,
	)
	last_name = models.CharField(
		_('last name'),
		blank=True,
		null=True,
		max_length=30,
	)
	email = models.EmailField(
		_('email address'),
		unique=True,
		blank=True,
		null=True,
	)
	phone_number = models.CharField(
		_('mobile phone'),
		unique=True,
		blank=True,
		null=True,
		max_length=20,
	)

	REQUIRED_FIELDS = ['email', 'last_name', 'first_name', 'phone_number']

	objects = AuthUserManager()

	def __str__(self):
		return self.username
