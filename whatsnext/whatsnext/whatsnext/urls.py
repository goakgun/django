from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'whatsnext.views.home', name='home'),

    url(r'^aboutus/$', 'whatsnext.views.aboutus', name='aboutus'),
    url(r'^contactus/$', 'whatsnext.views.contactus', name='contactus'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # related to users of urls
    (r'^user/',include('users.urls')),

)
