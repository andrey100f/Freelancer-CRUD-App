# Generated by Django 4.2.5 on 2023-09-23 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freelancer',
            old_name='tagLine',
            new_name='tagline',
        ),
    ]
