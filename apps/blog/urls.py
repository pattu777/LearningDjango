from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    url(r'^$', views.index, name='index'),
    
    # /blog/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    
    # /blog/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    
    # /blog/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]