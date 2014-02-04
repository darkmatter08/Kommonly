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
    url(r'^api/organizer/signup$', 'Kommonly.views.organizer_signup'),
    url(r'^organizer/home$', 'Kommonly.views.organizer_home'),
)

urlpatterns += patterns('organizer.views',
    # url(r'^staff/interview_status/$', 'interview_status'),
    url(r'^dashboard/$', 'show_dashboard'),
)
urlpatterns += patterns('sponsor.views',
    # url(r'^staff/interview_status/$', 'interview_status'),
    url(r'^company_dashboard/$', 'show_company_dashbaord'),
)
