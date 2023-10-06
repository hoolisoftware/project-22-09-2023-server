from rest_framework import serializers

from .. import models


# User Organization


class UserOrganizationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        exclude = ('owner',)


class UserOrganizationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'

    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class UserOrganizationRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        exclude = ('owner',)


# User Branch


class UserBranchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


class UserBranchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


class UserBranchRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'


# Admin Organization

class SuperadminOrganizationCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'


class SuperadminOrganizationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'
