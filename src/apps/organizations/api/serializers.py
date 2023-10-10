from rest_framework import serializers

from .. import models


class ReadOnlyModelSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields


class EmptySerializer(serializers.Serializer):
    pass

    def create(self, validated_data):
        return object()

    def update(self, instance, validated_data):
        return object()


# Superadmin

class SAdminOrganizationCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'


class SAdminBranchCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


class SAdminOfferCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class SAdminBetCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bet
        fields = '__all__'


# Organization Admin


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


# Branch Admin


class BAdminOrganizationRSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'


class BAdminBranchRUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'
        read_only_fields = ['administrators', 'organization']


class BAdminOfferRSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class BAdminBetRUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bet
        fields = '__all__'
        read_only_fields = ['branch']


# Staff


class StaffOrganizationRSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'


class StaffBranchRSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


class StaffOfferRSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class StaffBetRUSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bet
        fields = '__all__'
        read_only_fields = ['branch', 'table_number', 'bet', 'action_id']
