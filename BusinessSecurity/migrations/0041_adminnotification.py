# Generated by Django 3.2.7 on 2022-02-01 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BusinessSecurity', '0040_alter_orderprice_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_choice', models.CharField(choices=[('bcs', 'BCS'), ('pcs', 'PCS')], max_length=255)),
                ('notification', tinymce.models.HTMLField()),
                ('notification_time', models.DateTimeField()),
                ('is_read', models.BooleanField(default=False)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_notification_business', to='BusinessSecurity.business')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_notification_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
