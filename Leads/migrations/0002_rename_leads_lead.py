# Generated by Django 4.1.1 on 2022-09-30 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leads',
            new_name='Lead',
        ),
    ]