# Generated by Django 4.0.4 on 2022-05-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugTrackerApp', '0003_extendeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='nickname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
