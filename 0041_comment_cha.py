# Generated by Django 3.2.9 on 2022-03-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cha',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
