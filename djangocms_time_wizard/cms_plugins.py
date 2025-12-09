from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from polymorphic.admin import PolymorphicInlineSupportMixin
from time_wizard.admin import PeriodModelInline, TimeWizardModelAdmin

from djangocms_time_wizard.conf import (
    DJANGOCMS_TIME_WIZARD_COOKIE_NAME,
    DJANGOCMS_TIME_WIZARD_WRAPPER,
)
from djangocms_time_wizard.models import TimeWizardInlineModel, TimeWizardModel


class TimeWizardPluginBase(CMSPluginBase):
    module = _('Time Wizard')
    render_template = 'djangocms_time_wizard/time_wizard.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['show_wrapper'] = DJANGOCMS_TIME_WIZARD_WRAPPER
        context[
            'show_inactive_content'
        ] = self._show_inactive_content_from_cookie(context)
        return context

    def _show_inactive_content_from_cookie(self, context):
        cookie_value = context["request"].COOKIES.get(
            DJANGOCMS_TIME_WIZARD_COOKIE_NAME,
            "show-inactive-content:true",
        )
        for item in cookie_value.split("::"):
            key, val = item.split(":")
            if key == "show-inactive-content":
                return val == "true"
        return True


class TimeWizardPlugin(TimeWizardPluginBase):
    model = TimeWizardModel
    name = _('Time Wizard')


class TimeWizardInlinePlugin(PolymorphicInlineSupportMixin,
                             TimeWizardPluginBase):
    model = TimeWizardInlineModel
    name = _('Time Wizard (inline)')
    inlines = [PeriodModelInline]

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(
            TimeWizardModelAdmin.get_extra_selection_context(),
        )
        return super().add_view(
            request,
            form_url=form_url,
            extra_context=extra_context,
        )

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(
            TimeWizardModelAdmin.get_extra_selection_context(),
        )
        return super().change_view(
            request,
            object_id,
            form_url=form_url,
            extra_context=extra_context,
        )


plugin_pool.register_plugin(TimeWizardPlugin)
plugin_pool.register_plugin(TimeWizardInlinePlugin)
