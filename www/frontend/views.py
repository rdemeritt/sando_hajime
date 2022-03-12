from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


class UserLogin(LoginView):
    def get_success_url(self):
        last_login = self.request.user.last_login
        return super().get_success_url()
        pass


def index(request):
    fundraiser = {}
    return render(request, 'index.html', context=fundraiser)


def about(request):
    context = {}
    return render(request, 'about.html', context=context)


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
