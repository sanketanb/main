from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages
from django.contrib.messages import error

# render routes
def index(request):
    return render(request,"login_registration/index.html")

def quotes(request):
    try:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'quotes_display': Quote.objects.all()
        }
        return render(request,"login_registration/quotes.html", context)
    except:
        return redirect(reverse('lr:index'))

def logout(request):
    request.session.clear()
    return redirect(reverse('lr:index'))

# post routes
def register(request):
    if request.method == "POST":        
        result = User.objects.validate(request.POST)
        if type(result) == User:
        # we can also do if type(result) == list, but we consider the best ones first
            request.session['user_id'] = result.id
            messages.success(request, 'Successfully registered!!!')
            return redirect(reverse('lr:quotes'))
        else:
            for err in result:
                messages.error(request, err)            
    return redirect(reverse('lr:index'))

def login(request):
    if request.method == "POST":
        result = User.objects.validate_login(request.POST)
        if type(result) == User:            
            request.session['user_id'] = result.id
            messages.success(request, 'Successfully logged in!!!')
            return redirect(reverse('lr:quotes'))
        else:
            for err in result:
                messages.error(request, err)       
    return redirect(reverse('lr:index'))
        
def contribute(request):
    if request.method == "POST":    
        print("in contri")  
        desc= request.POST["desc"]  
        c=request.session['user_id']
        
        Quote.objects.create(desc=desc, author=User.objects.get(id=c))
        return redirect(reverse('lr:quotes'))       
    return redirect(reverse('lr:quotes'))

def fav(request):
    return redirect(reverse('lr:index')) 