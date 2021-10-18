from django.contrib import admin

from accounts.models.user import User

class UserAdmin(admin.ModelAdmin):
	model = User
