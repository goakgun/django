from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
url(r'^$', 'users.views.home', name='home'),
url(r'^signup/$', 'users.views.signup', name='signup'),
url(r'^logout/$', 'users.views.logout', name='logout'),


#auth
url(r'^login/$', 'users.views.login'),
url(r'^auth/$', 'users.views.auth_view'),
url(r'^logout/$', 'users.views.logout'),

#url(r'^register/$', 'users.views.register'),
#url(r'^register_success/$', 'users.views.register_success'),


)
