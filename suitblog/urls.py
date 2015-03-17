from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'suitblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('suitblog.posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
