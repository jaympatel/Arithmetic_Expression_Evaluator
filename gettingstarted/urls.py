from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import ExpressionEvaluation.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', hello.views.index, name='index'),
    url(r'^$', ExpressionEvaluation.views.get_expression, name='get_expression'),
    url(r'^get_expression',ExpressionEvaluation.views.get_expression, name='get_expression'),
    url(r'^db', ExpressionEvaluation.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
