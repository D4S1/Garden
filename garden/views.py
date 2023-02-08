from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class MainView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "main.html")


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("garden:main")
        return render(request, "login.html")


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return redirect('garden:login')
