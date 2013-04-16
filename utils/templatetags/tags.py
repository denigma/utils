# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse


register = template.Library()

@register.simple_tag
def active(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return "active"
    return ""

@register.simple_tag
def location(request):
    if request.path == '/':
        return ' » %s' % 'Home'
    return ' » %s' % request.path[1:-1].replace('/', ' » ').title()

#234567891123456789212345678931234567894123456789512345678961234567897123456789