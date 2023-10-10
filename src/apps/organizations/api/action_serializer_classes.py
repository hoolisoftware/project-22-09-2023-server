from apps.users.roles import ROLES
from . import serializers


def get_action_serializer_classes(
    _serializers
):
    action_serializer_classes = {}
    actions = ('list', 'create', 'update', 'partial_update', 'retrieve', 'metadata') # noqa

    for action in actions:
        action_serializer_classes[action] = {}

        for role in ROLES:
            if not (action in _serializers[role[0]][1]):
                action_serializer_classes[action][role[0]] = _serializers[role[0]][0] # noqa
            else:
                action_serializer_classes[action][role[0]] = serializers.EmptySerializer # noqa

    return action_serializer_classes


organization = get_action_serializer_classes({
    'superadmin': [
        serializers.SAdminOrganizationCRUDSerializer,
        []
    ],
    'organization_admin': [
        serializers.OAdminOrganizationCRUDSerializer,
        ['create']
    ],
    'branch_admin': [
        serializers.BAdminOrganizationRSerializer,
        [],
    ],
    'staff': [
        serializers.StaffOrganizationRSerializer,
        []
    ]
})


branch = get_action_serializer_classes({
    'superadmin': [
        serializers.SAdminBranchCRUDSerializer,
        []
    ],
    'organization_admin': [
        serializers.OAdminBranchCRUDSerializer,
        []
    ],
    'branch_admin': [
        serializers.BAdminBranchRUSerializer,
        ['create']
    ],
    'staff': [
        serializers.StaffBranchRSerializer,
        []
    ]
})


offer = get_action_serializer_classes({
    'superadmin': [
        serializers.SAdminOfferCRUDSerializer,
        []
    ],
    'organization_admin': [
        serializers.OAdminOfferCRUDSerializer,
        []
    ],
    'branch_admin': [
        serializers.BAdminOfferRSerializer,
        []
    ],
    'staff': [
        serializers.StaffOfferRSerializer,
        []
    ]
})


bet = get_action_serializer_classes({
    'superadmin': [
        serializers.SAdminBetCRUDSerializer,
        []
    ],
    'organization_admin': [
        serializers.OAdminBetCRUDSerializer,
        []
    ],
    'branch_admin': [
        serializers.BAdminBetRUSerializer,
        []
    ],
    'staff': [
        serializers.StaffBetRUSerializer,
        ['create']
    ]
})
