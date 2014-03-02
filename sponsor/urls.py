from django.conf.urls import patterns, url, include

urlpatterns = patterns('sponsor.views',
    url(r'^business_dashboard/$', 'show_business_dashboard'),
    # ex: /businesses
    url(r'^$', 'businesses', name="businesses"),
    # ex: businesses/google/
    url(r'^(?P<business_name>\w+)/$','business_profile', name='profile'),

)