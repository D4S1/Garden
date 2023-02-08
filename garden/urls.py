from django.urls import path
from . import views

app_name = 'garden'
urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('main', views.MainView.as_view(), name="main"),
    path('logout', views.LogoutView.as_view(), name="logout"),

]
