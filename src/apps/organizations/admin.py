from django.contrib import admin

from . import models


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
        'id',
        'created'
    )


@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'organization',
        'address',
        'id',
        'created'
    )


@admin.register(models.Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'organization',
        'team_a',
        'team_b',
        'action_id',
        'created'
    )


@admin.register(models.Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = (
        'organization',
        'branch',
        'table_number',
        'bet',
        'created'
    )
