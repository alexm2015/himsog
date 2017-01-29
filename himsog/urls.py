from django.conf.urls import url

from himsog.views import ContentPage
from himsog.views.content import ContentAddView
from himsog.views.home import Home
from himsog.views.home import Landing
from himsog.views.home import get_contents

homepatterns = [
    url(r'^$', Landing.as_view(), name="landing"),
    url(r'^home/$', Home.as_view(), name="home"),
    url(r'^get_contents/$', get_contents)
    # url(r'^(?P<category_slug>[-\w]+)/$', Home.as_view(), name="home"),
]

# Add list of patterns
contentpatterns = [
    url(r'^content/(?P<id>[0-9]+)/$', ContentPage.as_view(), name="content_page"),
    url(r'^content/add/$', ContentAddView.as_view(), name="content_add_page"),
]

urlpatterns = homepatterns + contentpatterns
