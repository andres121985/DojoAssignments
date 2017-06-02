from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$', views.index),
    url(r'^trucks$', views.trucks),
    url(r'^addtruck$', views.add_truck),
    url(r'^add$', views.add),
    url(r'^delete$', views.delete),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^search$', views.search),
    url(r'^category/(?P<id>\d+)$', views.category),
    url(r'^category/(?P<id>\d+)/(?P<truck_id>\d+)$', views.specific_truck),
]
