from django.urls import path

from accounts.views.login import LoginView
from accounts.views.user import UserView


urlpatterns = [
	path('login/', LoginView.as_view()),
	path('users/', UserView.as_view()),
	path('users/<int:id>/', UserView.as_view())
]
