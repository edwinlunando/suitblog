from django.conf.urls import patterns, url

urlpatterns = patterns('suitblog.contacts.views',
    url(r'^contact$', 'contact', name='contact'),

)
