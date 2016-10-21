from __future__ import unicode_literals
import datetime
from datetime import date
from ..login.models import User
from django.db import models

# Create your models here.

class TravelManager(models.Manager):
    def addPlans(self, postdata):
        user=User.objects.get(id=postdata['user'])
        plan=Travels.objects.create(dest=postdata['dest'], start=postdata['start'], end=postdata['end'], plan=postdata['plan'], user=user)
        return True
    def addJoin(self, u_id, d_id):
        plan=Travels.objects.get(id=d_id)
        user=User.objects.get(id=u_id)
        plan.joined.add(user)
        plan.save()
        return True
    def dateCheck(self, postdata):
        start=postdata['start']
        today=str(date.today())
        end=postdata['end']
        if start < today:
            return False
        if end < start:
            return False
        return True
    def contentCheck(self, postdata):
        if len(postdata['dest']) < 1 or len(postdata['plan']) < 1 or len(postdata['start']) < 1 or len(postdata['end']) < 1 :
            return False
        return True

class Travels(models.Model):
    dest=models.CharField(max_length=40)
    start=models.DateField()
    end=models.DateField()
    plan=models.CharField(max_length=80)
    user=models.ForeignKey('login.User', related_name='planner')
    joined=models.ManyToManyField('login.User', related_name='joined')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=TravelManager()
