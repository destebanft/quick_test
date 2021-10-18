from django.contrib import admin

from accounts.models.auth_user import AuthUser
from accounts.admin.auth_user import AuthUserAdmin
from accounts.models.user import User
from accounts.admin.user import UserAdmin

admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(User, UserAdmin)
