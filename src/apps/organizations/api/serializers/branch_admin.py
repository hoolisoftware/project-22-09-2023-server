from rest_framework import serializers

from . import ReadOnlyModelSerializer
from ... import models


class BAdminOrganizationCRUDSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'


class BAdminBranchCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'
        read_only_fields = ['administrators', 'organization']


class BAdminBranchRSerializer(BAdminBranchCRUDSerializer):
    organization = BAdminOrganizationCRUDSerializer()


class BAdminOfferCRUDSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class BadminOfferRSerializer():
    organization = BAdminOrganizationCRUDSerializer()


class BAdminBetCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bet
        fields = '__all__'
        read_only_fields = ['branch']
