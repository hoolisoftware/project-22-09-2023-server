from django.contrib.auth import get_user_model
from rest_framework import serializers

from ... import models

User = get_user_model()


class SAdminOrganizationCRUDSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        label='Owner username',
        help_text="Every user has it's own username, look to users page.",
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = models.Organization
        fields = [
            'id',
            'name',
            'owner',
            'created',
            'branches_count'
        ]


class SAdminBranchCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        exclude = [
            'administrators',
            'staff'
        ]


class SAdminBranchRSerializer(SAdminBranchCRUDSerializer):
    organization = SAdminOrganizationCRUDSerializer()


class SAdminOfferCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class SAdminOfferRSerializer(SAdminOfferCRUDSerializer):
    organization = SAdminOrganizationCRUDSerializer()


class SAdminBetCRUDSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(
        label='Branch ID',
        help_text="Every branch has it's own ID, look to branches page.",
        queryset=models.Branch.objects.all()
    )
    offer = serializers.PrimaryKeyRelatedField(
        label='Offer ID',
        help_text="Every offer has it's own ID, look to offers page.",
        queryset=models.Offer.objects.all()
    )

    class Meta:
        model = models.Bet
        fields = '__all__'


class SAdminBetRSerializer(SAdminBetCRUDSerializer):
    branch = SAdminBranchRSerializer()
    offer = SAdminOfferCRUDSerializer()
