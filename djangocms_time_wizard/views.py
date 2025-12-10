from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .conf import DJANGOCMS_TIME_WIZARD_COOKIE_NAME


@login_required
def admin_cookie_settings(request):
    cvalue = request.COOKIES.get(
        DJANGOCMS_TIME_WIZARD_COOKIE_NAME,
        "show-inactive-content:true",
    )
    checked = []
    for item in cvalue.split("::"):
        key, val = item.split(":")
        if val == "true":
            checked.append(key)
    context = {
        "cookie_name": DJANGOCMS_TIME_WIZARD_COOKIE_NAME,
        "available_ids": ["show-inactive-content"],
        "checked": checked,
    }
    return render(
        request,
        "djangocms_time_wizard/admin_cookie_settings.html",
        context,
    )
