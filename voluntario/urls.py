from django.conf.urls import patterns, include, url
from django.contrib import admin
from voluntario.core import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voluntario.views.home', name='home'),
    # url(r'^voluntario/', include('voluntario.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^voluntario/(?P<voluntario_id>\d+)/', views.dashboard),
    url(r'^$', views.index, "index"),
    url(r'^campanha/?$', views.campanha, name="campanha"),
    url(r'^campanha/(?P<id_campanha>\d+)/?^$', views.campanha_show, name="campanha-show"),
)
