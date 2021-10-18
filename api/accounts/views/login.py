import json

from django.contrib.auth.signals import user_logged_in
from django.http.response import HttpResponse
from rest_framework.views import APIView
from oauth2_provider.views.base import TokenView
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
from utils.response import error_handler
from accounts.models.auth_user import AuthUser
from accounts.models.user import User

class LoginView(APIView, TokenView):
	permission_classes = []

	@error_handler
	def post(self, request, *args, **kwargs):
		password = request.data.get('password', None)
		mobile_phone = request.data.get('mobile_phone', None)
		auth_user = AuthUser.objects.get(phone_number=mobile_phone)
		user_additional_data = User.objects.get(pk=auth_user)
		request._request.POST = request._request.POST.copy()
		request._request.POST['grant_type'] = 'password'
		request._request.POST['client_id'] = 'CI9xXluMc3JOxt7EM6INbq24bSxPXL6xQSG7148P'
		request._request.POST['password'] = password
		request._request.POST['username'] = auth_user.username
		
		_, headers, body, status = self.create_token_response(request._request)

		if status == 200:
			access_token = json.loads(body).get('access_token')
			if access_token is not None:
				token = get_access_token_model().objects.get(token=access_token)
				user_logged_in.send(sender=token.user.__class__, request=request, user=token.user)
				app_authorized.send(sender=self, request=request, token=token)
				body_json = json.loads(body)
				result = {
					'user':{
						'id': auth_user.id,
						'first_name': auth_user.first_name,
						'last_name': auth_user.last_name,
						'date_birth': str(user_additional_data.date_birth),
						'email': auth_user.email,
						'mobile_phone': auth_user.phone_number,
						'password': auth_user.password
					},
					'access_token': body_json['access_token'],
					'refresh_token': body_json['refresh_token']
				}
		response = HttpResponse(content=json.dumps(result), status=status)

		for k, v in headers.items():
			response[k] = v
		return response
