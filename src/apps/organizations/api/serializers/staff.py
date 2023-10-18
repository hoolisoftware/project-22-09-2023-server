from rest_framework import serializers
from . import ReadOnlyModelSerializer

from ... import models


class StaffOrganizationCRUDSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'


class StaffBranchCRUDSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


class StaffOfferCRUDSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class StaffBetCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bet
        fields = '__all__'
        read_only_fields = ['branch', 'table_number', 'bet', 'action_id']
