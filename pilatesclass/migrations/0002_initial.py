# Generated by Django 5.0.6 on 2024-07-31 03:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pilatesclass", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="pilatesclass",
            name="User_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="pilatesclass", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
