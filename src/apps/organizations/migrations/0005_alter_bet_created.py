# Generated by Django 4.2.5 on 2023-10-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_branch_administrator_bet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
