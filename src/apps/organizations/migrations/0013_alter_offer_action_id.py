# Generated by Django 4.2.5 on 2023-10-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0012_alter_offer_action_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='action_id',
            field=models.IntegerField(verbose_name='Action ID'),
        ),
    ]
