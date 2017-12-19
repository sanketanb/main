from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^quotes$', views.quotes, name='quotes'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^contribute$', views.contribute, name='contribute'),
    url(r'^fav$', views.fav, name='fav')
]