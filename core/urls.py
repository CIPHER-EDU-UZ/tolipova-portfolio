from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(),name=' login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('info', info , name="info")
]
