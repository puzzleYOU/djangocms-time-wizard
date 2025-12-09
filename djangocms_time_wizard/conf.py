from django.conf import settings

DJANGOCMS_TIME_WIZARD_WRAPPER = getattr(settings,
                                        'DJANGOCMS_TIME_WIZARD_WRAPPER',
                                        True)
DJANGOCMS_TIME_WIZARD_COOKIE_NAME = "djangocms-time-wizard-admin-settings"
