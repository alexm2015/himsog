from django.conf.urls import url

from himsog.views import HomePage
from himsog.views import CategoryContentListPage

homepatterns = [
    url(r'^$', HomePage.as_view(), name='index'),
]

# Add list of patterns
contentpatterns = []

urlpatterns = homepatterns + contentpatterns
