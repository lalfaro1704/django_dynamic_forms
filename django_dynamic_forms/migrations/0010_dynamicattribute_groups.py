# Generated by Django 2.0.2 on 2018-04-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('django_dynamic_forms', '0009_auto_20180423_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicattribute',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', verbose_name='groups'),
        ),
    ]
