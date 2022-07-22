# Generated by Django 3.2.7 on 2022-01-01 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_choice', models.CharField(choices=[('bcs', 'BCS'), ('pcs', 'PCS')], max_length=255)),
                ('nda', models.FileField(blank=True, null=True, upload_to='nda/')),
                ('nca', models.FileField(blank=True, null=True, upload_to='nca/')),
                ('quotation', models.FileField(blank=True, null=True, upload_to='quotation/')),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('extra_field', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_order', to='BusinessSecurity.order')),
            ],
        ),
    ]
