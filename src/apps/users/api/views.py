from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets

from . import serializers


User = get_user_model()


class UserSelfRetrieveAV(generics.RetrieveAPIView):
    serializer_class = serializers.UserSelfSerializer

    def get_object(self):
        return self.request.user


class UserSelfRetrieveUpdateAV(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserSelfRetrieveUpdateSeriazlizer

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserCrudSerializer

    def get_queryset(self):
        if self.request.user.role == 'superadmin':
            return User.objects.all()
        return User.objects.none()
