from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("signup/", views.UserRegistrationView.as_view(), name="signup"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("profile/", views.UserProfile.as_view(), name="profile"),
]
