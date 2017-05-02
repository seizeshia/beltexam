from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^quotedash$', views.quotedash),
    url(r'^logout$',views.logout),
    url(r'^addquote$',views.addquote),
    url(r'^favorite/(?P<id>\d+)$', views.favorite),
    url(r'^removefav/(?P<id>\d+)$', views.removefav),
    url(r'^quoteprofile/(?P<id>\d+)$', views.quoteprofile)
]
