from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, userManager
# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def process(request):
    error=0
    if not userManager.lengthCheck(request.POST['name'],request.POST['username']):
        messages.error(request, 'Name and Username must contain at least 3 characters.')
        error=1
    if not len(request.POST['pass1'])>7:
        messages.error(request,'Password must be at least 8 characters')
        error=1
    if not request.POST['pass1'] == request.POST['pass2']:
        messages.error(request, 'Passwords must match')
        error=1
    if userManager.uniqueUser(request.POST['username']):
        messages.error(request, 'That username is already taken.')
        error=1
    if error:
        return redirect('/')

    userManager.addUser(str(request.POST['name']),str(request.POST['username']),str(request.POST['pass1']))
    user=User.objects.get(username=str(request.POST['username']))
    request.session['id']=user.pk
    messages.add_message(request, messages.SUCCESS, 'Hello, '+user.name+'!')
    return redirect(reverse('exam:index'))

def login(request):
    error=0
    if not userManager.loginCheck(str(request.POST['username']), str(request.POST['pass'])):
        messages.error(request, 'A vaild username/password is required to login.')
        error=1
    if error:
        return redirect('/')
    if not userManager.passCheck(request.POST['username'],request.POST['pass']):
        messages.add_message(request, messages.ERROR, 'Username or password is incorrect.')
        error=1
    if error:
        return redirect('/')
    else:
        user=User.objects.get(username=request.POST['username'])
        request.session['id']=user.pk
        messages.add_message(request, messages.SUCCESS, 'Hello, '+user.name+'!')
        return redirect(reverse('exam:index'))


def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))
