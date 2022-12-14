# Generated by Django 4.0.2 on 2022-04-08 17:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0047_alter_contacts_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="categoryfirst",
            name="text_en",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="տեքստ"),
        ),
        migrations.AddField(
            model_name="categoryfirst",
            name="text_fa",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="տեքստ"),
        ),
        migrations.AddField(
            model_name="categoryfirst",
            name="text_hy",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="տեքստ"),
        ),
        migrations.AddField(
            model_name="categoryfirst",
            name="text_ru",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="տեքստ"),
        ),
        migrations.AddField(
            model_name="categoryfirst",
            name="title_en",
            field=models.CharField(max_length=100, null=True, verbose_name="Վերնագիր"),
        ),
        migrations.AddField(
            model_name="categoryfirst",
            name="title_fa",
            field=models.CharField(max_length=100, null=True, verbose_name="Վերնագիր"),
        ),
        migrations.AddField(
            model_name="categoryfirst",
            name="title_hy",
            field=models.CharField(max_length=100, null=True, verbose_name="Վերնագիր"),
        ),
        migrations.AddField(
            model_name="categoryfirst",
            name="title_ru",
            field=models.CharField(max_length=100, null=True, verbose_name="Վերնագիր"),
        ),
        migrations.AddField(
            model_name="categorylast",
            name="text_en",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="տեքստ"),
        ),
        migrations.AddField(
            model_name="categorylast",
            name="text_fa",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="տեքստ"),
        ),
        migrations.AddField(
            model_name="categorylast",
            name="text_hy",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="տեքստ"),
        ),
        migrations.AddField(
            model_name="categorylast",
            name="text_ru",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="տեքստ"),
        ),
        migrations.AddField(
            model_name="categorylast",
            name="title_en",
            field=models.CharField(max_length=100, null=True, verbose_name="Վերնագիր"),
        ),
        migrations.AddField(
            model_name="categorylast",
            name="title_fa",
            field=models.CharField(max_length=100, null=True, verbose_name="Վերնագիր"),
        ),
        migrations.AddField(
            model_name="categorylast",
            name="title_hy",
            field=models.CharField(max_length=100, null=True, verbose_name="Վերնագիր"),
        ),
        migrations.AddField(
            model_name="categorylast",
            name="title_ru",
            field=models.CharField(max_length=100, null=True, verbose_name="Վերնագիր"),
        ),
        migrations.AddField(
            model_name="pagetext",
            name="categoryi_en",
            field=models.CharField(
                choices=[("0", "news"), ("1", "shop")],
                max_length=100,
                null=True,
                verbose_name="նշեք էջը",
            ),
        ),
        migrations.AddField(
            model_name="pagetext",
            name="categoryi_fa",
            field=models.CharField(
                choices=[("0", "news"), ("1", "shop")],
                max_length=100,
                null=True,
                verbose_name="նշեք էջը",
            ),
        ),
        migrations.AddField(
            model_name="pagetext",
            name="categoryi_hy",
            field=models.CharField(
                choices=[("0", "news"), ("1", "shop")],
                max_length=100,
                null=True,
                verbose_name="նշեք էջը",
            ),
        ),
        migrations.AddField(
            model_name="pagetext",
            name="categoryi_ru",
            field=models.CharField(
                choices=[("0", "news"), ("1", "shop")],
                max_length=100,
                null=True,
                verbose_name="նշեք էջը",
            ),
        ),
        migrations.AddField(
            model_name="pagetext",
            name="texti_en",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="pagetext",
            name="texti_fa",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="pagetext",
            name="texti_hy",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="pagetext",
            name="texti_ru",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="shop",
            name="price_en",
            field=models.SmallIntegerField(null=True, verbose_name="արժեք"),
        ),
        migrations.AddField(
            model_name="shop",
            name="price_fa",
            field=models.SmallIntegerField(null=True, verbose_name="արժեք"),
        ),
        migrations.AddField(
            model_name="shop",
            name="price_hy",
            field=models.SmallIntegerField(null=True, verbose_name="արժեք"),
        ),
        migrations.AddField(
            model_name="shop",
            name="price_ru",
            field=models.SmallIntegerField(null=True, verbose_name="արժեք"),
        ),
        migrations.AddField(
            model_name="shop",
            name="title_en",
            field=models.CharField(max_length=17, null=True, verbose_name="վերնագիր"),
        ),
        migrations.AddField(
            model_name="shop",
            name="title_fa",
            field=models.CharField(max_length=17, null=True, verbose_name="վերնագիր"),
        ),
        migrations.AddField(
            model_name="shop",
            name="title_hy",
            field=models.CharField(max_length=17, null=True, verbose_name="վերնագիր"),
        ),
        migrations.AddField(
            model_name="shop",
            name="title_ru",
            field=models.CharField(max_length=17, null=True, verbose_name="վերնագիր"),
        ),
    ]
