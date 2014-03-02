from django.conf.urls import patterns, url, include

urlpatterns = patterns('sponsor.views',
    url(r'^business_dashboard/$', 'show_business_dashboard'),
    # ex: /businesses
    url(r'^$', 'businesses', name="businesses"),
    # ex: businesses/google/
    url(r'^(?P<business_id>\w+)/$','business_profile', name='profile'),
    url(r'^(?P<business_id>\w+)/contact','contact', name='contact'),

)