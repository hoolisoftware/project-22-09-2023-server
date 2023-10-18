from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, 'user')

urlpatterns = [
    path('me/', views.UserSelfRetrieveAV.as_view()),
    path('me/update/', views.UserSelfRetrieveUpdateAV.as_view())
] + router.urls
