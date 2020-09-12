# Generated by Django 3.0 on 2019-12-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0002_member_team"),
        ("team", "0002_auto_20191210_2330"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="heads",
            field=models.ManyToManyField(
                blank=True, related_name="heads", to="members.Member"
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="members",
            field=models.ManyToManyField(
                blank=True, related_name="members", to="members.Member"
            ),
        ),
    ]
