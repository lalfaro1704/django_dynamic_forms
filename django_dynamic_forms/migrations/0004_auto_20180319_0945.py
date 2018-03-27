# Generated by Django 2.0.3 on 2018-03-19 12:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_dynamic_forms', '0003_auto_20180313_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('key', models.CharField(max_length=100, verbose_name='key')),
                ('value', models.CharField(blank=True, max_length=256, null=True, verbose_name='value')),
            ],
            options={
                'verbose_name_plural': 'dynamic parameters',
                'verbose_name': 'dynamic parameter',
            },
        ),
        migrations.RemoveField(
            model_name='dynamicoptionselects',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='dynamicoptionselects',
            name='parent',
        ),
        migrations.AlterModelOptions(
            name='dynamicform',
            options={'verbose_name': 'dynamic form,.', 'verbose_name_plural': 'dynamic forms'},
        ),
        migrations.RemoveField(
            model_name='dynamicattribute',
            name='field_type',
        ),
        migrations.RemoveField(
            model_name='dynamicattribute',
            name='name',
        ),
        migrations.AddField(
            model_name='dynamicattribute',
            name='default_value',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='default value'),
        ),
        migrations.AddField(
            model_name='dynamicattribute',
            name='element_type',
            field=models.CharField(choices=[('input', 'input'), ('textarea', 'textarea'), ('checkbox', 'checkbox'), ('radio', 'radio'), ('select', 'select'), ('div', 'div'), ('label', 'label'), ('button', 'button'), ('i', 'i'), ('p', 'p'), ('h1', 'h1'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6')], default=None, max_length=100, verbose_name='element type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dynamicattribute',
            name='id_element',
            field=models.CharField(default=None, max_length=256, verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dynamicattribute',
            name='order',
            field=models.IntegerField(default=1, verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dynamicattribute',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_dynamic_forms.DynamicAttribute', verbose_name='parent'),
        ),
        migrations.AddField(
            model_name='dynamicform',
            name='action',
            field=models.CharField(blank=True, help_text='Specifies an address (url) where to submit the form (default: the submitting page).', max_length=256, null=True, verbose_name='action'),
        ),
        migrations.AddField(
            model_name='dynamicform',
            name='enctype',
            field=models.CharField(blank=True, help_text='Specifies the encoding of the submitted data (default: is url-encoded).', max_length=256, null=True, verbose_name='enctype'),
        ),
        migrations.AddField(
            model_name='dynamicform',
            name='method',
            field=models.CharField(blank=True, help_text='Specifies the HTTP method used when submitting the form (default: GET).', max_length=256, null=True, verbose_name='method'),
        ),
        migrations.AddField(
            model_name='dynamicform',
            name='order',
            field=models.IntegerField(default=1, verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dynamicform',
            name='target',
            field=models.CharField(blank=True, help_text='Specifies the target of the address in the action attribute (default: _self).', max_length=256, null=True, verbose_name='target'),
        ),
        migrations.AddField(
            model_name='simpleoptionselects',
            name='parent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='django_dynamic_forms.DynamicAttribute', verbose_name='parent'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dynamicform',
            name='code',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='code'),
        ),
        migrations.DeleteModel(
            name='DynamicOptionSelects',
        ),
        migrations.AddField(
            model_name='dynamicattribute',
            name='parameters',
            field=models.ManyToManyField(to='django_dynamic_forms.DynamicParameter', verbose_name='parameters'),
        ),
    ]