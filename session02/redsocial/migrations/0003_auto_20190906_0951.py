# Generated by Django 2.2.4 on 2019-09-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0002_auto_20190901_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hastag',
            name='hastag',
            field=models.CharField(help_text='Escriba su hashtag, debe contener menos de 20 caracteres', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Escriba su email verdadero', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(help_text='Escriba su nombre de usuario', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_status_update_comments',
            name='body',
            field=models.TextField(help_text='Escriba su comentorio'),
        ),
        migrations.AlterField(
            model_name='user_status_update_comments',
            name='date',
            field=models.DateField(help_text='Fecha de la seccion de comentarios'),
        ),
        migrations.AlterField(
            model_name='user_status_updates',
            name='body',
            field=models.TextField(help_text='Escriba la descripción del Estado'),
        ),
        migrations.AlterField(
            model_name='user_status_updates',
            name='date',
            field=models.DateField(help_text='Escriba la fecha de modificacion'),
        ),
    ]
