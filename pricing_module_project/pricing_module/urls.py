# pricing_module/urls.py

from django.urls import path
from .views import calculate_price_view
# from pricing_module.views import your_root_view

urlpatterns = [
    path('calculate_price/', calculate_price_view, name='calculate_price'),
    # path('', your_root_view, name='root_view'),
]

