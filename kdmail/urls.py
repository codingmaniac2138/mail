from django.conf.urls import include, url
from django.contrib import admin
from kdmail import views

urlpatterns = [
    url(r'^results/$', views.filter_res_view),
    url(r'^$',views.welcome),
    url(r'^register/$', views.register_view),
    url(r'^login/$', views.login_view),
    url(r'^auth/$', views.auth_view),
    # url(r'^loggedin/$', views.loggedin_view),
    url(r'^logout/$', views.logout_view),
    url(r'^invalid/$', views.invalid_view),
    url(r'^confirm/(?P<activation_key>\w+)/', views.register_confirm),
    url(r'^add_ids/$', views.add_ids_view),
]
