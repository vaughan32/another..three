# Generated by Django 4.1.1 on 2022-10-02 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0009_category_orgarnization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='orgarnization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leads.userprofile'),
        ),
    ]
