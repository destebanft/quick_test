from rest_framework import serializers

from accounts.models.user import User


class UserSerializer(serializers.ModelSerializer):

  email = serializers.SerializerMethodField()
  first_name = serializers.SerializerMethodField()
  last_name = serializers.SerializerMethodField()
  mobile_phone = serializers.SerializerMethodField()
  id = serializers.SerializerMethodField()

  def get_email(self, obj):
    return obj.auth_user.email

  def get_id(self, obj):
    return obj.auth_user_id

  def get_mobile_phone(self, obj):
    return obj.auth_user.phone_number

  def get_first_name(self, obj):
    return obj.auth_user.first_name

  def get_last_name(self, obj):
    return obj.auth_user.last_name
    
  class Meta:
    model = User
    fields = [
      'id',
      'first_name',
      'last_name',
			'date_birth',
      'mobile_phone',
      'email',
      'address'
		]
