# Generated by Django 3.2.9 on 2022-02-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Մութքագրման դաշտ')),
                ('chois', models.CharField(choices=[('հեռախոսահամար', 'հեռախոսահամար'), ('Ել․հասցե', 'Ել․հասցե'), ('Հասցե', 'Հասցե')], max_length=15, verbose_name='Տեսակ')),
            ],
            options={
                'verbose_name': 'Տվյալ',
                'verbose_name_plural': 'Տվյալներ',
            },
        ),
    ]
