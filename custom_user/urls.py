from django.urls import path
from custom_user.views.Register_View import RegisterView
from custom_user.views.Login_view import LoginView
from custom_user.views.UserProfile_view import UserProfile_view,EditUserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('userProfile/',UserProfile_view.as_view(),name='user_profile'),
    path('editUserProfile/',EditUserProfileView.as_view(),name='edit_user_profile')
]
