from django.apps import apps
from django.contrib.auth.models import UserManager


class AuthUserManager(UserManager):

	def _create_user(self, username, password, email=None, phone_number=None, require_ep=True, **extra_fields):
		"""
		Create and save a user with the given username, email or phone number, and password.
		"""
		if not username:
			raise ValueError('The given username must be set')

		if require_ep and not email and not phone_number:
			raise ValueError('Either email or phone_number must be set, both can not be None')

		if email:
			email = self.normalize_email(email)

		# Lookup the real model class from the global app registry so this
		# manager method can be used in migrations. This is fine because
		# managers are by definition working on the real model.
		GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)

		username = GlobalUserModel.normalize_username(username)
		user = self.model(username=username, email=email, phone_number=phone_number, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, password, email=None, phone_number=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, password, email, phone_number, **extra_fields)

	def create_superuser(self, username, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(username, password, require_ep=False, **extra_fields)
