from django.contrib import admin


from . import models


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
        'id'
    )


@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'organization',
        'address',
        'id'
    )
