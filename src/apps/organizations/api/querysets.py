from django.contrib.auth import get_user_model
from typing import Iterable
from ..models import Organization, Branch, Offer, Bet


User = get_user_model()


def get_organizations(
    user,
) -> Iterable[Organization]:
    return {
        'superadmin': Organization.objects.all(),
        'organization_admin': Organization.objects.filter(owner=user),
        'branch_admin': Organization.objects.filter(branches__administrators=user), # noqa
        'staff': Organization.objects.filter(branches__staff=user), # noqa
    }[user.role]


def get_branches(
    user,
) -> Iterable[Branch]:
    return {
        'superadmin': Branch.objects.all(),
        'organization_admin': Branch.objects.filter(organization__owner=user), # noqa
        'branch_admin': user.controlled_branches.all(),
        'staff': user.staff_branches.all()

    }[user.role]


def get_offers(
    user,
) -> Iterable[Offer]:
    return {
        'superadmin': Offer.objects.all(),
        'organization_admin': Offer.objects.filter(organization__owner=user), # noqa
        'branch_admin': Offer.objects.filter(organization__branches__in=user.controlled_branches.all()).all(), # noqa
        'staff': Offer.objects.filter(organization__branches__in=user.staff_branches.all()).all() # noqa
    }[user.role]


def get_bets(
    user
) -> Iterable[Bet]:
    return {
        'superadmin': Bet.objects.all(),
        'organization_admin': Bet.objects.filter(branch__organization__owner=user), # noqa
        'branch_admin': Bet.objects.filter(branch__administrators=user),
        'staff': Bet.objects.filter(branch__staff=user)
    }[user.role]
