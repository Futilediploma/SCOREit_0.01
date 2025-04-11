# Generated by Django 5.1.7 on 2025-04-02 18:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leagues", "0004_league_session_alter_league_season_alter_league_sex"),
    ]

    operations = [
        migrations.AddField(
            model_name="league",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="league",
            name="session",
            field=models.CharField(default="", max_length=20),
        ),
    ]
