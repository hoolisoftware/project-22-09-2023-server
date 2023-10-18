from rest_framework import serializers

from ... import models


class OAdminOrganizationCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class OAdminBranchCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


class OAdminOfferCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class OAdminBetCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bet
        fields = '__all__'
