from django.contrib.auth import get_user_model

from utils.response import ResponseError

User = get_user_model()


def get_existing_user(email, raise_error=True):
	try:
		user = User.objects.get(email=email)
	except User.DoesNotExist:
		if raise_error:
			raise ResponseError("user_does_not_exist", 400)
		return None
	return user
