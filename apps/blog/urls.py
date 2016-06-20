from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # /blog/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]