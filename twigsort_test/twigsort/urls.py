from django.conf.urls import patterns, include, url
from hello_world.views import hello, homepage, current_time, hours_ahead

# Uncomment next two lines to enable admin:
from django.contrib import admin
admin.autodiscover()

""" 
    This variable will be traced from the URLconf module.
    urlpattern: map between URLs and code that handles URLs
    from url import, we pass regex of hello URL and 
    our views 'hello' function.
"""

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^$',homepage),
    url(r'^current_time/$',current_time),
    # making dynamic urls
    # use regex to match any two digits
    # parenthis around regex passes data to view function
    url(r'^time/plus/(\d{1,2})/$', hours_ahead), # Matches one or two digits
    
)
