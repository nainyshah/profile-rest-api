# Generated by Django 2.2 on 2020-07-24 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='create_on',
            new_name='created_on',
        ),
    ]
