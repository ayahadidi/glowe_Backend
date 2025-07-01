from django.urls import path
from custom_user.views.Register_View import RegisterView
from custom_user.views.Login_view import LoginView
from custom_user.views.UserProfile_view import UserProfile_view,EditUserProfileView
from custom_user.views.passwordforgot_view import PasswordResetRequestView, PasswordResetConfirmView
urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('userProfile/',UserProfile_view.as_view(),name='user_profile'),
    path('editUserProfile/',EditUserProfileView.as_view(),name='edit_user_profile'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
