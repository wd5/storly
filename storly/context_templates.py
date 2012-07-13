# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from shop.models import Settings

def common_vars(request):
    """
    Function creates common context for all templates.
    """
    try:
        settings = Settings.objects.get(pk=1)
    except ObjectDoesNotExist:
        settings = {}
    return {
        'site_settings': settings,
        'domain': request.get_host(),
        }

