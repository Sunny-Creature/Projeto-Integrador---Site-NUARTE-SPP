from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from dashboard.models import UserLogin

# Create your views here.
def dashboard(request):
    context = {
        "user_login": UserLogin.objects.all(),
    }
    return render(request, 'dashboard/dashboard.html', context)