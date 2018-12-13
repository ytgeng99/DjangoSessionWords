from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_word$', views.add_word),
    url(r'^clear$', views.clear)
]