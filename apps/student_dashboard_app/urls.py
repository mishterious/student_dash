from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^add_user$', views.add_user), 
    url(r'^login$', views.login),
    url(r'^wish_list/(?P<id>\d+)$', views.wish_list),
    url(r'^wish_list/add', views.add_wish),
    url(r'^make_wish', views.make_wish),
    url(r'^add_to_wishlist/(?P<id>\d+)', views.add_to_wishlist),
    url(r'^wish_time', views.wish_time),
    url(r'^new_item/(?P<id>\d+)', views.new_item),
    url(r'^dashboard', views.dashboard),
    url(r'^delete/(?P<id>\d+)', views.delete),
    url(r'^remove_from_list/(?P<id>\d+)', views.remove),
    url(r'^logout$', views.logout),
]