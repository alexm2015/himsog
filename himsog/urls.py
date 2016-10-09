from django.conf.urls import url

from himsog.views import HomePage
from himsog.views.category import CategoryView

homepatterns = [
    url(r'^$', HomePage.as_view(), name='index'),
]

# Add list of patterns
contentpatterns = [
    url(r'^category/$', CategoryView.as_view(), name='index')
]

urlpatterns = homepatterns + contentpatterns
