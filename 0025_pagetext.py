# Generated by Django 3.2.9 on 2022-03-10 13:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_shop_shopcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='pagetext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('news', 'News'), ('shop', 'Shop')], max_length=100, verbose_name='նշեք էջը')),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Էջի մեկնաբանություն',
                'verbose_name_plural': 'Էջի մեկնաբանություներ',
            },
        ),
    ]
