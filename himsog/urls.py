from django.conf.urls import url


from himsog.views.home import Home
from himsog.views import ContentPage

homepatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'^(?P<category_slug>[-\w]+)/$', Home.as_view(), name="home"),
]

# Add list of patterns
contentpatterns = [
    url(r'^content/(?P<id>[0-9]+)/$', ContentPage.as_view(), name="content_page"),
]

urlpatterns = homepatterns + contentpatterns
