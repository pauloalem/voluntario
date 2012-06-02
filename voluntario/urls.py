from django.conf.urls import patterns, include, url
from django.contrib import admin
from voluntario.core import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'core.views.home', name='home'),
    
    # facebook
    url(r'^facebook/login/?$', 'facebook.views.login', name="facebook_login"),
    url(r'^facebook/authentication_callback/?$', 'facebook.views.authentication_callback'),
    url(r'^facebook/connect/?$', 'facebook.views.connect', name="facebook_connect"),
    url(r'^facebook/connect_callback/?$', 'facebook.views.connect_callback'),
    url(r'^facebook/setup/?$', 'core.views.facebook_setup', name="facebook_setup"),
    
    #user
    url(r'^user/register/?$', 'core.views.user_register', name="user_register"),
    url(r'^user/edit/?$', 'core.views.user_edit', name="user_edit"),
    url(r'^user/login/?$', 'core.views.user_login', name="user_login"),
    url(r'^user/remember_password/?$', 'core.views.remember_password', name="remember_password"),
    url(r'^user/logout/?$', 'django.contrib.auth.views.logout', name="user_logout"),
    url(r'^usuario/(?P<username>[a-zA-Z0-9\-\_\.]+)/?$', 'core.views.perfil', name="user_profile"),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
)
