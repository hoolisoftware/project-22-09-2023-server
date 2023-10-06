from rest_framework import viewsets
from django.core.exceptions import PermissionDenied


from .. import models
from . import serializers


class UserOrganizationViewSet(viewsets.ModelViewSet):
    action_serializer_classes = {
        'create': serializers.UserOrganizationCreateSerializer,
        'update': serializers.UserOrganizationRUDSerializer,
        'partial_update': serializers.UserOrganizationRUDSerializer,
        'retrieve': serializers.UserOrganizationRUDSerializer,
        'list': serializers.UserOrganizationListSerializer,
        'metadata': serializers.UserOrganizationRUDSerializer
    }

    def get_queryset(self):
        return self.request.user.organizations.all()

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        return self.action_serializer_classes[self.action]


class UserBranchViewSet(viewsets.ModelViewSet):
    action_serializer_classes = {
        'create': serializers.UserBranchCreateSerializer,
        'update': serializers.UserBranchRUDSerializer,
        'partial_update': serializers.UserBranchRUDSerializer,
        'retrieve': serializers.UserBranchRUDSerializer,
        'list': serializers.UserBranchListSerializer,
        'metadata': serializers.UserBranchRUDSerializer
    }

    def get_queryset(self):
        return models.Branch.objects.filter(organization__owner=self.request.user) # noqa

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action]
        except AttributeError:
            raise PermissionDenied()
