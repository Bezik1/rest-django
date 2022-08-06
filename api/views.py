from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from django.views.generic import TemplateView

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class HomeView(TemplateView):
    template_name = "index.html"