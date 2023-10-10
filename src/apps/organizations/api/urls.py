from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet, basename='organization'), # noqa
router.register(r'branches', views.BranchViewSet, basename='branch'),
router.register(r'offers', views.OfferViewSet, basename='offer'),
router.register(r'bets', views.BetViewSet, basename='bet')

urlpatterns = (
    path('', include(router.urls)),
)
