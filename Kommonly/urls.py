# Shawn Jain 
# 2/3/2014
# Kommonly project

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Kommonly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Kommonly.views.home'),
    (r'^/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

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
urlpatterns += patterns('sponsor.views',
    url(r'^business_dashboard/$', 'show_business_dashbaord'),
    url(r'^businesses$', 'get_businesses'),

)
urlpatterns += patterns('events.views',
    url(r'^events/create$', 'create_event'),
)
