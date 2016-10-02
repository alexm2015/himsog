from django.conf.urls import url

from himsog.views import HomePage

homepatterns = [
    url(r'^$', HomePage.as_view(), name='index'),
]

# Add list of patterns
contentpatterns = []

urlpatterns = homepatterns + contentpatterns
