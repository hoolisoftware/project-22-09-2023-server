from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # noqa
    path('admin/', admin.site.urls),

    path('api/organizations/', include('apps.organizations.api.urls'))
)
