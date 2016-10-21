from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Travels
import datetime
from datetime import date
from ..login.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
import types

# Create your views here.

def idCheck(request):
    if 'id' not in request.session:
        messages.add_message(request, messages.ERROR, 'Please login to continue.')
        return False
    else:
        return True

def index(request):
    if not idCheck(request):
        return redirect(reverse('login:index'))
    user=User.objects.get(id=request.session['id'])
    context={
        'user':user,
        'mytravel':Travels.objects.filter(user=user),
        'othertravel':Travels.objects.exclude(user=user),
    }
    return render(request, 'exam1/index.html', context)

def join(request, d_id):
    if not idCheck(request):
        return redirect(reverse('login:index'))
    Travels.objects.addJoin(request.session['id'],d_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def add(request):
    if not idCheck(request):
        return redirect(reverse('login:index'))
    context={
        'today':date.today()
    }
    return render(request, 'exam1/add.html', context)

def create(request):
    if not request.POST:
        return redirect(reverse('exam:index'))
    if not idCheck(request):
        return redirect(reverse('login:index'))
    if not Travels.objects.contentCheck(request.POST):
        messages.error(request, 'Please fill out all fields')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    if not Travels.objects.dateCheck(request.POST):
        messages.error(request, 'Dates must be occur after today with Travel Date To occuring after Travel Date From.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    try:
        travel=Travels.objects.addPlans(request.POST)
    except NameError:
        messages.error(request, 'Dates must be in MM/DD/YYYY format.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    return redirect(reverse('exam:index'))

def show(request, d_id):
    if not idCheck(request):
        return redirect(reverse('login:index'))
    context={
        'trip':Travels.objects.filter(id=d_id),

    }
    return render(request, 'exam1/dest.html', context)
