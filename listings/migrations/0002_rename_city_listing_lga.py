# Generated by Django 3.2.13 on 2022-06-05 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='city',
            new_name='lga',
        ),
    ]
