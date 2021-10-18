from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.db import IntegrityError

from utils.response import error_handler, ResponseSuccess, ResponseError
from accounts.models.user import User
from accounts.models.auth_user import AuthUser
from accounts.serializers.user import UserSerializer




class UserView(APIView):
	permission_classes = []

	@error_handler
	def get(self, request):
		user = User.objects.all()
		user_json = UserSerializer(user, many=True, context={'request': request}).data
		return Response(user_json, status=status.HTTP_200_OK)
