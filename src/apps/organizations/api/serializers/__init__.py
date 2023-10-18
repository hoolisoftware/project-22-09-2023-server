from rest_framework import serializers


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


from .superadmin         import * # noqa
from .organization_admin import * # noqa
from .branch_admin       import * # noqa
from .staff              import * # noqa