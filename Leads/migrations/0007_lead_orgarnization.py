# Generated by Django 4.1.1 on 2022-10-01 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0006_alter_lead_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='orgarnization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Leads.userprofile'),
            preserve_default=False,
        ),
    ]
