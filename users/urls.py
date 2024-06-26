from django.contrib.auth.views import (LoginView, LogoutView)
from django.urls import path
from users.apps import UsersConfig
from users import views

name = UsersConfig.name

urlpatterns = [
    path('user_profile/<int:pk>', views.UserDetailView.as_view(), name='user_profile'),
    path('user_profile_change/<int:pk>', views.UserChangeView.as_view(), name='user_change'),
    path('login/', LoginView.as_view(), name='user_log_in'),
    path('logout/', LogoutView.as_view(), name='user_log_out'),
    path('registration/', views.UserCreateView.as_view(), name='registration'),
    path('email-confirm/<str:token>/', views.verification, name='email-confirm'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.ResetComplete.as_view(), name='password-confirm'),
]
