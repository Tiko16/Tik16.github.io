# Generated by Django 3.2.9 on 2022-03-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20220310_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetext',
            name='categoryi',
            field=models.CharField(choices=[('0', 'news'), ('1', 'shop')], max_length=100, verbose_name='նշեք էջը'),
        ),
    ]