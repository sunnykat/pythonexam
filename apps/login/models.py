from __future__ import unicode_literals
from django.contrib import messages
import re
import bcrypt
from django.db import models
import datetime
from datetime import date

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(models.Model):
     name=models.CharField(max_length=15)
     username=models.CharField(max_length=15)
     pass_hash=models.CharField(max_length=255)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now=True)

class UserManager(models.Manager):
    def passCheck(self, postusername, postPass):
        user=User.objects.get(username=postusername)
        passhash=user.pass_hash
        if bcrypt.checkpw(postPass, passhash):
            return True

    def lengthCheck(self, postname, postusername):
        if len(postname) < 3:
            return False
        if len(postusername) < 3:
            return False
        return True

    def loginCheck(self, postusername, postpass):
        if len(postusername) < 3:
            return False
        if len(postpass) < 8:
            return False
        return True

    def passwordLength(self, passw):
        if len(passw) < 8:
            return False
        return True

    def uniqueUser(self, postusername):
        user=User.objects.filter(username=postusername)
        print user
        if user == []:
            return True
        else:
            return False

    def addUser(self, postname, postusername,postpass):
        newhash=bcrypt.hashpw(postpass, bcrypt.gensalt())
        User.objects.create(name=postname,username=postusername,pass_hash=newhash)
        return True

userManager=UserManager()
