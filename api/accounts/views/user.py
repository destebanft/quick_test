from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.db import IntegrityError

from utils.response import error_handler, ResponseSuccess, ResponseError
from accounts.models.user import User
from accounts.models.auth_user import AuthUser
from accounts.serializers.user import UserSerializer




class UserView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	@error_handler
	def get(self, request):
		user = User.objects.all()
		user_json = UserSerializer(user, many=True, context={'request': request}).data
		return Response(user_json, status=status.HTTP_200_OK)


	@error_handler
	def post(self, request):
		username = request.data.get('email', None)
		password = request.data.get('password', None)
		email = request.data.get('email', None)
		first_name = request.data.get('first_name', None)
		last_name = request.data.get('last_name', None)

		try:
			user = AuthUser.objects.create_user(
				username=username,
				password=password,
				email=email,
				first_name = first_name,
				last_name = last_name
			)
		except IntegrityError:
			return ResponseError("user_with_given_username_already_exists", status.HTTP_400_BAD_REQUEST)

		date_birth = request.data.get('date_birth', None)
		address = request.data.get('address', None)

		User.objects.create(
			auth_user=user,
			date_birth = date_birth,
			address = address
		)

		return ResponseSuccess("user_created", status=status.HTTP_200_OK)

	@error_handler
	def put(self, request, id=None):
		user = User.objects.get(auth_user=id)
		auth_user = AuthUser.objects.get(id=id)
		auth_user.first_name = request.data.get('first_name', user.auth_user.first_name)
		auth_user.last_name = request.data.get('last_name', user.auth_user.last_name)
		auth_user.phone_number = request.data.get('mobile_phone', user.auth_user.phone_number)
		auth_user.email = request.data.get('email', user.auth_user.email)
		auth_user.password = request.data.get('password', user.address)
		user.date_birth = request.data.get('date_birth', user.date_birth)
		user.address = request.data.get('address', user.address)
		auth_user.save()
		user.save()
		user = User.objects.get(auth_user=id)
		user_json = UserSerializer(user, context={'request': request}).data
		return ResponseSuccess(user_json, status=status.HTTP_200_OK)
	
	@error_handler
	def delete(self, request, id=None):
		user = User.objects.get(auth_user=id)
		auth_user = AuthUser.objects.get(id=id)
		auth_user.delete()
		user.delete()
		return ResponseSuccess("user_deleted", status=status.HTTP_200_OK)