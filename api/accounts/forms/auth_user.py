from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField

from accounts.models.auth_user import AuthUser


class AuthUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = AuthUser
		fields = ('username',)


class AuthUserChangeForm(UserChangeForm):
	class Meta:
		model = AuthUser
		fields = '__all__'
		field_classes = {'username': UsernameField}
