

from django.db import models

class PricingConfig(models.Model):
    name = models.CharField(max_length=255, unique=True, default=0.0)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    additional_price_per_km = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    time_multiplier_threshold_1 = models.PositiveIntegerField(default=0.02)  # in minutes
    time_multiplier_factor_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    time_multiplier_threshold_2 = models.PositiveIntegerField(default=0.0)  # in minutes
    time_multiplier_factor_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    waiting_charge_threshold = models.PositiveIntegerField(default=0.0)  # in seconds
    waiting_charge_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    distance_tier_threshold = models.PositiveIntegerField(default=0.0)  # in kilometers
    distance_tier_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    days_of_week = models.CharField(max_length=10, blank=True, null=True, default=0.0)  # Comma-separated list of days, e.g., "Mon,Tue,Wed"
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class PricingConfigStatus(models.Model):
    config = models.OneToOneField(PricingConfig, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"Status for {self.config.name}"
