import rest_framework.filters
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied

from .. import models
from . import action_serializer_classes
from . import querysets
from . import filters


viewset_http_method_names = [m for m in viewsets.ModelViewSet.http_method_names if m not in ['delete']] # noqa


class SerializerMixin:
    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.request.user.role][self.action] # noqa
        except KeyError:
            raise PermissionDenied()

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, pk=None):
        pass


class OrganizationViewSet(SerializerMixin, viewsets.ModelViewSet): # noqa
    http_method_names = viewset_http_method_names
    model = models.Organization
    action_serializer_classes = action_serializer_classes.organization
    filter_backends = [rest_framework.filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return querysets.get_organizations(self.request.user)


class BranchViewSet(SerializerMixin, viewsets.ModelViewSet):
    http_method_names = viewset_http_method_names
    model = models.Branch
    action_serializer_classes = action_serializer_classes.branch
    filterset_class = filters.BranchFilter

    def get_queryset(self):
        return querysets.get_branches(self.request.user)


class OfferViewSet(SerializerMixin, viewsets.ModelViewSet):
    http_method_names = viewset_http_method_names
    model = models.Offer
    action_serializer_classes = action_serializer_classes.offer

    def get_queryset(self):
        return querysets.get_offers(self.request.user)


class BetViewSet(SerializerMixin, viewsets.ModelViewSet):
    http_method_names = viewset_http_method_names
    model = models.Bet
    action_serializer_classes = action_serializer_classes.bet

    def get_queryset(self):
        return querysets.get_bets((self.request.user))
