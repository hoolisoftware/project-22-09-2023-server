from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Organization(models.Model):
    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    name = models.CharField('Name', max_length=64)
    owner = models.ForeignKey(verbose_name='Owner', to=User, related_name='organizations', on_delete=models.CASCADE) # noqa
    created = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<Organiznation ({self.id}) {self.name}>'


class Branch(models.Model):
    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    administrators = models.ManyToManyField(verbose_name='Administrator', to=User, related_name='controlled_branches', blank=True) # noqa
    staff = models.ManyToManyField(verbose_name='Staff', to=User, related_name='staff_branches', blank=True) # noqa
    address = models.TextField('Address')
    organization = models.ForeignKey(verbose_name='Organization', to=Organization, related_name='branches', on_delete=models.CASCADE) # noqa
    created = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.organization} / {self.address}'

    def __repr__(self) -> str:
        return f'<Branch ({self.organization.id}.{self.id})>'


class Offer(models.Model):
    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'

    organization = models.ForeignKey(verbose_name='Organization', to=Organization, related_name='offers', on_delete=models.CASCADE) # noqa
    action_id = models.IntegerField('Action ID')
    team_a = models.TextField('Team A wins')
    team_b = models.TextField('Team B wins')
    created = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.organization} {self.action_id}'

    def __repr__(self) -> str:
        return f'<Offer {self.organization} {self.organization.id} / {self.id}'


class Bet(models.Model):
    class Meta:
        verbose_name = 'Bet'
        verbose_name_plural = 'Bets'

    BET = (
        ('a', 'Team A wins'),
        ('b', 'Team B wins')
    )

    action_id = models.PositiveIntegerField('Action ID')
    branch = models.ForeignKey(verbose_name='Branch', to=Branch, related_name='bets', on_delete=models.CASCADE) # noqa    
    table_number = models.PositiveIntegerField('Table number')
    bet = models.CharField(max_length=1, choices=BET)
    created = models.DateTimeField(auto_now=True)
    paid = models.BooleanField('Paid', default=False)

    def __str__(self) -> str:
        return f'{self.branch.organization} / {self.branch} / {self.table_number} / {self.bet}' # noqa

    def __repr__(self) -> str:
        return f'<Bet {self.id}>'

    @property
    def organization(self):
        return self.branch.organization
