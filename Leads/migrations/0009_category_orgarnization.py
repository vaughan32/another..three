# Generated by Django 4.1.1 on 2022-10-02 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0008_category_lead_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='orgarnization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Leads.userprofile'),
        ),
    ]
