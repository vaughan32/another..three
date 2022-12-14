# Generated by Django 4.1.1 on 2022-10-01 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0003_remove_user_address_remove_user_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='orgarnization',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Leads.userprofile'),
            preserve_default=False,
        ),
    ]
