from apps.users.roles import ROLES
from . import serializers


def get_action_serializer_classes(
    _serializers
):
    action_serializer_classes = {}
    actions = ('list', 'create', 'update', 'partial_update', 'retrieve', 'metadata') # noqa

    for role in [i[0] for i in ROLES]:
        action_serializer_classes[role] = {}

        for action in actions:
            if action in _serializers[role]['special'].keys():
                action_serializer_classes[role][action] = _serializers[role]['special'][action] # noqa
            elif action in _serializers[role]['actions']:
                action_serializer_classes[role][action] = _serializers[role]['default'] # noqa
            else:
                action_serializer_classes[role][action] = serializers.EmptySerializer # noqa

    return action_serializer_classes


organization = get_action_serializer_classes({
    'superadmin': {
        'default': serializers.SAdminOrganizationCRUDSerializer,
        'special': {},
        'actions': ['list', 'create', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    },
    'organization_admin': {
        'default': serializers.OAdminOrganizationCRUDSerializer,
        'special': {},
        'actions': ['list', 'update', 'partial_update', 'retrieve', 'metadata']
    },
    'branch_admin': {
        'default': serializers.BAdminOrganizationCRUDSerializer,
        'special': {},
        'actions': ['list', 'retrieve', 'metadata']
    },
    'staff': {
        'default': serializers.StaffOrganizationCRUDSerializer,
        'special': {},
        'actions': ['list', 'retrieve', 'metadata']
    }
})


branch = get_action_serializer_classes({
    'superadmin': {
        'default': serializers.SAdminBranchCRUDSerializer,
        'special': {
            'list': serializers.SAdminBranchRSerializer,
            'retrieve': serializers.SAdminBranchRSerializer
        },
        'actions': ['list', 'create', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    },
    'organization_admin': {
        'default': serializers.OAdminBranchCRUDSerializer,
        'special': {
            'list': serializers.SAdminBranchRSerializer,
            'retrieve': serializers.SAdminBranchRSerializer
        },
        'actions': ['list', 'create', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    },
    'branch_admin': {
        'default': serializers.BAdminBranchCRUDSerializer,
        'special': {},
        'actions': ['list', 'update', 'partial_update', 'retrieve', 'metadata']
    },
    'staff': {
        'default': serializers.StaffBranchCRUDSerializer,
        'special': {},
        'actions': ['list', 'retrieve', 'metadata']
    }
})


offer = get_action_serializer_classes({
    'superadmin': {
        'default': serializers.SAdminOfferCRUDSerializer,
        'special': {
            'list': serializers.SAdminOfferRSerializer,
            'retrieve': serializers.SAdminOfferRSerializer
        },
        'actions': ['list', 'create', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    },
    'organization_admin': {
        'default': serializers.OAdminOfferCRUDSerializer,
        'special': {},
        'actions': ['list', 'create', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    },
    'branch_admin': {
        'default': serializers.BAdminOfferCRUDSerializer,
        'special': {},
        'actions': ['list', 'update', 'partial_update', 'retrieve', 'metadata']
    },
    'staff': {
        'default': serializers.StaffOfferCRUDSerializer,
        'special': {},
        'actions': ['list', 'retrieve', 'metadata']
    }
})


bet = get_action_serializer_classes({
    'superadmin': {
        'default': serializers.SAdminBetCRUDSerializer,
        'special': {
            'list': serializers.SAdminBetRSerializer,
            'retrieve': serializers.SAdminBetRSerializer
        },
        'actions': ['list', 'create', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    },
    'organization_admin': {
        'default': serializers.OAdminBetCRUDSerializer,
        'special': {},
        'actions': ['list', 'create', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    },
    'branch_admin': {
        'default': serializers.BAdminBetCRUDSerializer,
        'special': {},
        'actions': ['list', 'create', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    },
    'staff': {
        'default': serializers.StaffBetCRUDSerializer,
        'special': {},
        'actions': ['list', 'update', 'partial_update', 'retrieve', 'metadata'] # noqa
    }
})
