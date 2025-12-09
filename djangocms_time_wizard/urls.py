from django.urls import path

from .views import admin_cookie_settings

urlpatterns = [
    path(
        "time-wizard-cookie-settings/",
        admin_cookie_settings,
        name="djangocms-time-wizard-cookie-settings",
    )
]
