from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import ExpressionEvaluation.views

urlpatterns = patterns('',

    url(r'^$', ExpressionEvaluation.views.get_expression, name='get_expression'),
    url(r'^get_expression',ExpressionEvaluation.views.get_expression, name='get_expression'),
    url(r'^admin/', include(admin.site.urls)),

)
