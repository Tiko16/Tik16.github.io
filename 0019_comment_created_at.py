# Generated by Django 3.2.9 on 2022-03-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20220304_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField("2021-01-05 06:00:00.000000-09:00"),
            preserve_default=False,
        ),
    ]