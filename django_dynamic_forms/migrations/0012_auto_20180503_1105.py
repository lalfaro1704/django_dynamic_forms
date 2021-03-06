# Generated by Django 2.0.2 on 2018-05-03 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_dynamic_forms', '0011_auto_20180502_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicattribute',
            name='id_element',
            field=models.CharField(default=django.utils.timezone.now, help_text='Value for HTML attribute (id="example").', max_length=256, unique=True, verbose_name='id'),
            preserve_default=False,
        ),
    ]
