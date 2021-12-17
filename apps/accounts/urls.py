from django.contrib.auth import views as auth_views
from django.urls import path

from .views import LoginView, Home, RegistrationView

app_name = "accounts"

urlpatterns = [

    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegistrationView.as_view(), name="register"),
    path('', Home.as_view(), name="home"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
