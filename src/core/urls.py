from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = (
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # noqa
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # noqa
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # noqa
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # noqa
    path('admin/', admin.site.urls),

    path('api/organizations/', include('apps.organizations.api.urls')),
    path('api/users/', include('apps.users.api.urls'))
)
