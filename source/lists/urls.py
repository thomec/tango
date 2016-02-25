# lists/urls.py


from django.conf.urls import include, url

from lists import views


urlpatterns = [
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^new$', views.new_list2, name='new_list'),
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]
