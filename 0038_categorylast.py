# Generated by Django 3.2.9 on 2022-03-21 17:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_categoryfirst_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryLast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Վերնագիր')),
                ('text', ckeditor.fields.RichTextField(verbose_name='տեքստ')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='categoryfirst', verbose_name='նկար')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategorykey', to='main.categoryfirst')),
            ],
        ),
    ]
