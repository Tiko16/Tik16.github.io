# Generated by Django 3.2.9 on 2022-02-28 18:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='text',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='նկարագիր'),
            preserve_default=False,
        ),
    ]
