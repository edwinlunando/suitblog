from django.conf.urls import patterns, url

urlpatterns = patterns('suitblog.posts.views',
    url(r'^posts$', 'posts', name='posts'),
    url(r'^posts/(?P<slug>[-\w]+)$', 'detail', name='detail'),
)
