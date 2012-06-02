import json, urllib

from django.db import models
from django.contrib.auth.models import User
from core.models import UsuarioPromessa

class FacebookProfile(models.Model):
    user = models.OneToOneField(User, related_name="facebook_profile")
    
    facebook_id = models.BigIntegerField()
    access_token = models.CharField(max_length=150)

    def get_facebook_profile(self):
        fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token=%s' % self.access_token)
        return json.load(fb_profile)
    
    def prometer(self, promessa):
        up = UsuarioPromessa()
        up.usuario = self
        up.promessa = promessa
        up.save()
