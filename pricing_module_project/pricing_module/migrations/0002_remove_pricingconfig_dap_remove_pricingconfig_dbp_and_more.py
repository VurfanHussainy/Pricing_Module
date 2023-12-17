# Generated by Django 4.2.6 on 2023-12-17 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricing_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricingconfig',
            name='dap',
        ),
        migrations.RemoveField(
            model_name='pricingconfig',
            name='dbp',
        ),
        migrations.RemoveField(
            model_name='pricingconfig',
            name='tmf',
        ),
        migrations.RemoveField(
            model_name='pricingconfig',
            name='wc',
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='additional_price_per_km',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='distance_tier_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='distance_tier_threshold',
            field=models.PositiveIntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='is_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='name',
            field=models.CharField(default=0.0, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='time_multiplier_factor_1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='time_multiplier_factor_2',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='time_multiplier_threshold_1',
            field=models.PositiveIntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='time_multiplier_threshold_2',
            field=models.PositiveIntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='waiting_charge_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='pricingconfig',
            name='waiting_charge_threshold',
            field=models.PositiveIntegerField(default=0.0),
        ),
        migrations.AlterField(
            model_name='pricingconfig',
            name='days_of_week',
            field=models.CharField(blank=True, default=0.0, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='PricingConfigStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_enabled', models.BooleanField(default=True)),
                ('config', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pricing_module.pricingconfig')),
            ],
        ),
    ]