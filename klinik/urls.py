from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^printTest/', 'profil.views.printTest'),
 #    url(r'^testPeter/$', 'dokument.views.testPeter'),
 #   url(r'^testPeter2/$',
 #       'dokument.views.contact'),
    url(r'^admin/dokument/arbejdsseddel/pdf/(?P<arbj_id>\d+)/$',
         'dokument.views.printPDF'),
    url(r'^filldb/', 'kartotek.views.filldata'),
    # Examples:
                       # url(r'^$', 'klinik.views.home', name='home'),
    # url(r'^klinik/', include('klinik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
