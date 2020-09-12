# Generated by Django 2.2.5 on 2020-02-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_auto_20200207_2216"),
    ]

    operations = [
        migrations.RemoveField(model_name="event", name="date_time",),
        migrations.AddField(
            model_name="event",
            name="date",
            field=models.DateField(default="2020-02-02"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="time",
            field=models.TimeField(default="22:00:00"),
            preserve_default=False,
        ),
    ]
