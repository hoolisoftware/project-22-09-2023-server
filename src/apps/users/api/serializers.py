from rest_framework import serializers

from .. import models


class UserSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserSelfRetrieveUpdateSeriazlizer(serializers.ModelSerializer):
    password = serializers.CharField(help_text='Leave blank to not set password.', write_only=True, required=False) # noqa

    class Meta:
        model = models.User
        fields = [
            'username',
            'password'
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()

        return instance


class UserCrudSerializer(serializers.ModelSerializer):
    password = serializers.CharField(help_text='Leave blank to not set password.', write_only=True, required=False) # noqa

    class Meta:
        model = models.User
        fields = [
            'id',
            'username',
            'role',
            'password'
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.role = validated_data.get('role')
        if validated_data.get('password', ''):
            instance.set_password(validated_data.get('password', ''))
        instance.save()

        return instance

    def create(self, validated_data):
        obj = models.User.objects.create(**validated_data)
        if validated_data.get('password', ''):
            obj.set_password(validated_data.get('password'))
        obj.save()
        return obj
