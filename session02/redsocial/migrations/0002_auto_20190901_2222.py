# Generated by Django 2.2.4 on 2019-09-02 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['email'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
