# Generated by Django 2.0.3 on 2018-03-13 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_dynamic_forms', '0002_auto_20180306_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dynamicattribute',
            options={'verbose_name': 'dynamic attribute', 'verbose_name_plural': 'dynamic attributes'},
        ),
        migrations.AlterModelOptions(
            name='dynamicform',
            options={'verbose_name': 'dynamic form', 'verbose_name_plural': 'dynamic forms'},
        ),
        migrations.AlterModelOptions(
            name='dynamicoptionselects',
            options={'verbose_name': 'dynamic option select', 'verbose_name_plural': 'dynamic option select'},
        ),
        migrations.AlterModelOptions(
            name='formattribute',
            options={'verbose_name': 'form attribute', 'verbose_name_plural': 'form attribute'},
        ),
        migrations.AlterModelOptions(
            name='simpleoptionselects',
            options={'verbose_name': 'simple option select', 'verbose_name_plural': 'simple option select'},
        ),
    ]