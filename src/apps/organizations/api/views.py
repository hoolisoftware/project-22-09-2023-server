from rest_framework import viewsets
from django.core.exceptions import PermissionDenied

from .. import models
from . import action_serializer_classes
from . import querysets


viewset_http_method_names = [m for m in viewsets.ModelViewSet.http_method_names if m not in ['delete']] # noqa


class OrganizationViewSet(viewsets.ModelViewSet): # noqa
    http_method_names = viewset_http_method_names
    model = models.Organization
    action_serializer_classes = action_serializer_classes.organization

    def destroy(self, request, pk=None):
        pass

    def get_queryset(self):
        return querysets.get_organizations(self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action][self.request.user.role] # noqa
        except KeyError:
            raise PermissionDenied()


class BranchViewSet(viewsets.ModelViewSet):
    http_method_names = viewset_http_method_names
    model = models.Branch
    action_serializer_classes = action_serializer_classes.branch

    def get_queryset(self):
        return querysets.get_branches(self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action][self.request.user.role] # noqa
        except KeyError:
            raise PermissionDenied()


class OfferViewSet(viewsets.ModelViewSet):
    http_method_names = viewset_http_method_names
    model = models.Offer
    action_serializer_classes = action_serializer_classes.offer

    def get_queryset(self):
        return querysets.get_offers(self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action][self.request.user.role] # noqa
        except KeyError:
            raise PermissionDenied()


class BetViewSet(viewsets.ModelViewSet):
    http_method_names = viewset_http_method_names
    model = models.Bet
    action_serializer_classes = action_serializer_classes.bet

    def get_queryset(self):
        return querysets.get_bets((self.request.user))

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action][self.request.user.role] # noqa
        except KeyError:
            raise PermissionDenied(())
