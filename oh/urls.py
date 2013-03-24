from django.conf.urls import patterns, include, url
from oh import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oh.views.home', name='home'),
    url(r'^$', 'kinect.views.index', name='index'),
    url(r'^(?P<player_id>\d+)$', 'kinect.views.player', name='player'),
    url(r'^simpleemotion/$', 'kinect.views.simpleemotion', name='simpleemotion'),
    url(r'^emotiongraph/(?P<player_id>\d+)/(?P<session_id>\d+)$', 'kinect.views.emotiongraph', name='emotiongraph'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
            (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
    )

urlpatterns += patterns('',
            (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
