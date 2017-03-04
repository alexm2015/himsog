from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

# from himsog.views import ContentPage
from himsog.views.content import ContentAddView
from himsog.views.content import ContentView
from himsog.views.home import Home
from himsog.views.home import Landing


homepatterns = [
    url(r'^$', Landing.as_view(), name='landing'),
    url(r'^home/$', Home.as_view(), name="home"),
#     url(r'^(?P<category_slug>[-\w]+)/$', Home.as_view(), name="home"),
]

# Add list of patterns
contentpatterns = [
    url(r'^content/(?P<content_id>[0-9]+)/$', ContentView.as_view(), name='content_page'),
    url(r'^content/add/$', ContentAddView.as_view(), name='content_add_page'),
]

authpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = homepatterns + contentpatterns + authpatterns
