# Generated by Django 3.2.9 on 2022-03-22 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_comment_cha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='cha',
        ),
    ]
