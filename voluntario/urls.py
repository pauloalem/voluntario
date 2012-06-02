from django.conf.urls import patterns, include, url
from django.contrib import admin
from voluntario.core import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'core.views.home', name='home'),
    
    # facebook
    url(r'^facebook/login/?$', 'voluntario.facebook.views.login', name="facebook_login"),
    url(r'^facebook/authentication_callback/?$', 'voluntario.facebook.views.authentication_callback'),
    url(r'^facebook/connect/?$', 'voluntario.facebook.views.connect', name="facebook_connect"),
    url(r'^facebook/connect_callback/?$', 'voluntario.facebook.views.connect_callback'),
    url(r'^facebook/setup/?$', 'voluntario.core.views.facebook_setup', name="facebook_setup"),
    
    #user
    url(r'^user/register/(?P<type>[a-zA-Z]+)/?$', 'voluntario.core.views.user_register', name="user_register"),
    url(r'^user/edit/(?P<type>[a-zA-Z]+)/?$', 'voluntario.core.views.user_edit', name="user_edit"),
    url(r'^user/login/?$', 'voluntario.core.views.user_login', name="user_login"),
    url(r'^user/remember_password/?$', 'voluntario.core.views.remember_password', name="remember_password"),
    url(r'^user/logout/?$', 'django.contrib.auth.views.logout', name="user_logout"),
    url(r'^usuario/(?P<username>[a-zA-Z0-9\-\_\.]+)/?$', 'voluntario.core.views.perfil', name="user_profile"),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^voluntario/(?P<voluntario_id>\d+)/', 'voluntario.core.views.dashboard', name='dashboard'),
    url(r'^$', views.index, "index"),
    url(r'^campanha/?$', views.campanha, name="campanha"),
    url(r'^campanha/(?P<id_campanha>\d+)/?^$', views.campanha_show, name="campanha-show"),
)
