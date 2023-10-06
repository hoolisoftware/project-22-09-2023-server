from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'organizations', views.UserOrganizationViewSet, basename='organization'), # noqa
router.register(r'branches', views.UserBranchViewSet, basename='branch')

urlpatterns = (
    path('', include(router.urls)),
)
