# Generated by Django 2.2.24 on 2021-11-26 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0002_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Grocessory',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Vegitable',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lentil',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rice',
        ),
    ]