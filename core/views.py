from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')

