import cgi, urllib, json

from django.conf import settings

from facebook.models import FacebookProfile

class FacebookComponent(object):
    
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        
    def get_access_token(self, code, redirect_uri):
        args = {
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'redirect_uri': redirect_uri,
            'code': code,
        }

        # Get a legit access token
        target = urllib.urlopen('https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(args)).read()
        response = cgi.parse_qs(target)
        access_token = response['access_token'][-1]
        
        return access_token
    
    def get_facebook_profile(self, access_token):
        fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token=%s' % access_token)
        fb_profile = json.load(fb_profile)
        
        return fb_profile
    
    def get_app_friends(self, access_token):
        app_friends = urllib.urlopen('https://api.facebook.com/method/friends.getAppUsers?access_token=%s&format=json' % access_token)
        app_friends = json.load(app_friends)
        
        return app_friends
    
    def connect_facebook(self, token, request):
        try:
            if request.user.facebook_profile:
                return None
        except:
            pass
    
        args = {
            'client_id': settings.FACEBOOK_APP_ID,
            'client_secret': settings.FACEBOOK_APP_SECRET,
            'redirect_uri': request.build_absolute_uri('/facebook/connect_callback'),
            'code': token,
        }

        # Get a legit access token
        target = urllib.urlopen('https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(args)).read()
        response = cgi.parse_qs(target)
        access_token = response['access_token'][-1]

        # Read the user's profile information
        fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token=%s' % access_token)
        fb_profile = json.load(fb_profile)
        
        try:
            # Try and find existing user
            fb_user = FacebookProfile.objects.get(facebook_id=fb_profile['id'])
            
            if fb_user:
                return False

        except FacebookProfile.DoesNotExist:
            try:
                # Create the FacebookProfile
                fb_user = FacebookProfile(user=request.user, facebook_id=fb_profile['id'], access_token=access_token)
                fb_user.save()
                return True
            except:
                return None

        