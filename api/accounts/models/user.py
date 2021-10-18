from django.db import models

from accounts.models.auth_user import AuthUser
from managers.base_manager import BaseManager



class User(models.Model):
	auth_user = models.OneToOneField(
		AuthUser,
		on_delete=models.CASCADE,
		related_name="additional_data",
		primary_key=True,
	)
	date_birth = models.DateField()
	address = models.CharField(
		max_length=50
	)
	
	
	
	objects = BaseManager()

	@property
	def username(self):
		return self.auth_user.username

	def __str__(self):
		return self.username
