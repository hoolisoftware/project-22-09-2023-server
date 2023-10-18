from django_filters import rest_framework as filters

from .. import models


class BranchFilter(filters.FilterSet):
    class Meta:
        model = models.Branch
        fields = ('organization', )
