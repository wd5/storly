# -*- coding: utf-8 -*-

from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from shop.models import Slider
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    try:
        slide = Slider.objects.get(pk=1)
    except ObjectDoesNotExist:
        slide = {}
    context = {
            'slide':slide,
            }
    return direct_to_template(request, 'home.html', context)