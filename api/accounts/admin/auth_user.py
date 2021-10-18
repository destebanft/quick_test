from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.forms.auth_user import AuthUserCreationForm, AuthUserChangeForm
from accounts.models.auth_user import AuthUser


class AuthUserAdmin(UserAdmin):
	add_form = AuthUserCreationForm
	form = AuthUserChangeForm
	model = AuthUser
	list_display = ('username', 'is_staff', 'is_active',)
	list_filter = ('is_active',)
	fieldsets = (
		(None, {
			'fields': ('username', 'password', 'email', 'first_name', 'last_name')
		}),
		(_('Permissions'), {
			'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
		(_('Important dates'), {
			'fields': ('last_login', 'date_joined')
		}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'password1', 'password2', 'email', 'phone_number')}
		 ),
	)
	search_fields = ('username',)
	ordering = ('username',)
