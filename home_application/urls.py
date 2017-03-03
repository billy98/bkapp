# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(  '',
    url(r'^', 'home_application.views.index'),
)

