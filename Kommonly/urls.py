from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Kommonly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^businesses/', include('sponsor.urls',namespace="sponsor", app_name="sponsor")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Kommonly.views.home'),
    (r'^/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^/assets/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('organizer.views',
    # url(r'^staff/interview_status/$', 'interview_status'),
    url(r'^api/organizer/signup$', 'organizer_signup'),
    url(r'^api/organizer/login$', 'organizer_login'),
    url(r'^organizer/home$', 'organizer_home'),
    url(r'^api/organizer/newEvent$', 'newEvent'),
    url(r'^dashboard/$', 'show_dashboard'),
    url(r'^api/organizer/getAllEvents$', 'getAllEvents'),
    url(r'^signup$', 'signup'),
    url(r'^logout$', 'logout'),
)

urlpatterns += patterns('events.views',
    url(r'^events/create$', 'create_event'),
    url(r'^events/(\d{1,5})/edit$', 'edit_event'),
)
