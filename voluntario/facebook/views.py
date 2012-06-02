# -*- coding: utf-8 -*-
import urllib

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

from facebook import FacebookComponent

def login(request):
    """ First step of process, redirects user to facebook, which redirects to authentication_callback. """

    args = {
        'client_id': settings.FACEBOOK_APP_ID,
        'scope': settings.FACEBOOK_SCOPE,
        'redirect_uri': request.build_absolute_uri('/facebook/authentication_callback'),
    }
    return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))

def authentication_callback(request):
    """ Second step of the login process.
    It reads in a code from Facebook, then redirects back to the home page. """
    code = request.GET.get('code')
    
    if not code:
        return HttpResponseRedirect(reverse('homepage'))
        
    user = authenticate(token=code, request=request)

    if user.is_anonymous():
        #we have to set this user up
        url = reverse('facebook_setup')
        url += "?code=%s" % code

        resp = HttpResponseRedirect(url)

    else:
        auth_login(request, user)

        #figure out where to go after setup
        url = getattr(settings, "LOGIN_REDIRECT_URL", "/")

        resp = HttpResponseRedirect(url)
    
    return resp

def connect(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse('homepage'))
    
    try:
        if request.user.facebook_profile:
            return HttpResponseRedirect(reverse('homepage'))
    except:
        pass
    
    args = {
        'client_id': settings.FACEBOOK_APP_ID,
        'scope': settings.FACEBOOK_SCOPE,
        'redirect_uri': request.build_absolute_uri('/facebook/connect_callback'),
    }
    
    return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))

def connect_callback(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse('homepage'))
    
    try:
        if request.user.facebook_profile:
            return HttpResponseRedirect(reverse('homepage'))
    except:
        pass
    
    code = request.GET.get('code')
    
    if not code:
        return HttpResponseRedirect(reverse('homepage'))
    
    fb_component = FacebookComponent(app_id=settings.FACEBOOK_APP_ID, app_secret=settings.FACEBOOK_APP_SECRET)
        
    response = fb_component.connect_facebook(token=code, request=request)
    
    if response == False:
        request.session['sys_message'] = 'Sua conta do facebook já está associada a outra conta do prometo.me.'
    elif response == None:
        request.session['sys_message'] = 'Não foi possível efetuar a associação da sua conta do facebook no momento.'
        
    return HttpResponseRedirect(reverse('dashboard'))
