# Generated by Django 4.1.7 on 2023-02-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="created_at",
        ),
    ]
