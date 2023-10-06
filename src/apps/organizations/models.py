from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Organization(models.Model):
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    name = models.CharField('Название', max_length=64)
    owner = models.ForeignKey(verbose_name='Владалец', to=User, related_name='organizations', on_delete=models.CASCADE) # noqa

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<Organiznation ({self.id}) {self.name}>'


class Branch(models.Model):
    class Meta:
        verbose_name = 'Ветка'
        verbose_name_plural = 'Ветки'

    address = models.TextField('Адресс')
    organization = models.ForeignKey(verbose_name='Организация', to=Organization, on_delete=models.CASCADE) # noqa

    def __str__(self) -> str:
        return self.address

    def __repr__(self) -> str:
        return f'<Branch ({self.organization.id}.{self.id})>'
