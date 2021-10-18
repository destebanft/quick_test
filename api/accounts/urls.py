from django.urls import path

from accounts.views.login import LoginView
from accounts.views.user import UserView
from accounts.views.user_security import UserSecurityView


urlpatterns = [
	path('users/login/', LoginView.as_view()),
	path('users/', UserView.as_view()),
	path('user/<int:id>/', UserSecurityView.as_view())
]
