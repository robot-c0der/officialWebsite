# Generated by Django 2.1.7 on 2019-12-10 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0002_auto_20191210_2330'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('funding', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('extra', models.TextField()),
                ('members', models.ManyToManyField(to='members.Member')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
    ]
