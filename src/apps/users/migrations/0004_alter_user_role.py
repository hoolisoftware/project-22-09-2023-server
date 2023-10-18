# Generated by Django 4.2.5 on 2023-10-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('superadmin', 'Superadmin'), ('organization_admin', 'Organization admin'), ('branch_admin', 'Branch admin'), ('staff', 'Staff')], help_text='This fields defines what user capable to do', max_length=32, verbose_name='Role'),
        ),
    ]