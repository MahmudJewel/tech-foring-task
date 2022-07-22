# Generated by Django 3.2.7 on 2022-01-01 06:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0005_quotation_agree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='additional_info',
        ),
        migrations.AddField(
            model_name='quotation',
            name='quotation_info',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
