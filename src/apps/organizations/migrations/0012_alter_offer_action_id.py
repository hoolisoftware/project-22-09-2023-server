# Generated by Django 4.2.5 on 2023-10-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_alter_branch_options_remove_bet_action_id_bet_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='action_id',
            field=models.IntegerField(unique=True, verbose_name='Action ID'),
        ),
    ]