# Generated by Django 3.0 on 2019-12-12 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0003_auto_20191212_1426"),
    ]

    operations = [
        migrations.RemoveField(model_name="team", name="members",),
    ]
