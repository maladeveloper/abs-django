# Generated by Django 2.2.5 on 2019-12-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abs_immigration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abs_immigration',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
