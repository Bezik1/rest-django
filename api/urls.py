from rest_framework import routers
from django.urls import include, path

from .views import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)), #inclue dodaje urls z router do głównej ścieżki
]
