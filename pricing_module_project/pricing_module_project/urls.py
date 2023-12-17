"""
URL configuration for pricing_module_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import path, include
from pricing_module.urls import urlpatterns as pricing_module_urls  # Adjust the import statement as needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate_price/', include('pricing_module.urls')),
    path('', include(pricing_module_urls)),
]









# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("pricing/", include("pricing_module.urls")),
#     path('', RedirectView.as_view(url="pricing/calculate_pricing/")), # Redirect root path to "pricing/"
# ]

# if settings.DEBUG:
#     urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
