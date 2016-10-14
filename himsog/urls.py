from django.conf.urls import url


from himsog.views import HomePage
from himsog.views import ContentPage
from himsog.views.category import CategoryView
from himsog.views import CategoryContentListPage

homepatterns = [
    url(r'^$', HomePage.as_view(), name='index'),
]

# Add list of patterns
contentpatterns = [
	url(r'^content/(?P<id>[0-9]+)/$', ContentPage.as_view(), name="content_page"),
    url(r'^category/$', CategoryView.as_view(), name='index'),
]

categorypatterns = [
	url(r'^cat/(?P<category_slug>[-\w]+)/$', CategoryContentListPage.as_view(), name="content_list_page"),
]

urlpatterns = homepatterns + categorypatterns + contentpatterns
