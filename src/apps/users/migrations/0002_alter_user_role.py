# Generated by Django 4.2.5 on 2023-10-05 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('superadmin', 'Superadmin'), ('organization_admin', 'Organization Admin'), ('branch_admin', 'Branch Admin'), ('staff', 'Staff')], max_length=32, verbose_name='Роль'),
        ),
    ]
