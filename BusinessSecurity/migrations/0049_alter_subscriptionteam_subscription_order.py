# Generated by Django 3.2.7 on 2022-02-03 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0048_subscriptionteam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionteam',
            name='subscription_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptionteam_subscriptionorder', to='BusinessSecurity.subscriptionorder'),
        ),
    ]
