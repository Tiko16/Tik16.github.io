# Generated by Django 3.2.9 on 2022-04-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_remove_comment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
