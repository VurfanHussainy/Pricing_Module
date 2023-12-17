
from django import forms
from .models import PricingConfig, PricingConfigStatus
from django.contrib.admin.models import LogEntry, CHANGE

class PricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = '__all__'  # Use all fields from the model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Log who is changing the configuration along with the timestamp
        user = self.request.user if hasattr(self, 'request') and self.request.user.is_authenticated else None
        if user:
            instance.save()

            # Log the change
            LogEntry.objects.log_action(
                user_id=user.id,
                content_type_id=None,  # Set to None for custom models
                object_id=instance.id,
                object_repr=str(instance),
                action_flag=CHANGE,
                change_message="Pricing configuration modified.",
            )

        return instance

class PricingConfigStatusForm(forms.ModelForm):
    class Meta:
        model = PricingConfigStatus
        fields = ['is_enabled']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
