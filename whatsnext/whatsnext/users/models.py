from django.db import models
from django.utils.encoding import smart_unicode

class User(models.Model):

    first_name = models.CharField(max_length=120, null=False, blank=False)
    last_name = models.CharField(max_length=120, null=False, blank=False)
    username = models.CharField(max_length=120, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=True,auto_now=False)
    
    def __unicode__(self):
        return smart_unicode(self.email, self.username)
    
    
