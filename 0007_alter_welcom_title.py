# Generated by Django 3.2.9 on 2022-02-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_welcom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcom',
            name='title',
            field=models.CharField(max_length=68, verbose_name='վերնագր'),
        ),
    ]