# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response

from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Greeting, guestbook_key, DEFAULT_GUESTBOOK_NAME
from django.core.context_processors import csrf

def main_page(request):
    
    guestbook_name = request.GET.get('guestbook_name',
            DEFAULT_GUESTBOOK_NAME)
    
    greetings_query = Greeting.query(ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
    #greetings_query = Greeting.query().order(-Greeting.date)
    greetings = greetings_query.fetch(10)
    
    template_values = Context({
            # 'user':      user,
            'greetings': greetings,
            #'guestbook_name': guestbook_name,
            #'url': url,
            #'url_linktext': url_linktext,
            })
    # need for POST
    template_values.update(csrf(request))
    
    return HttpResponse(loader.get_template('guestbook/index.html').render(template_values))

def sign_post(request):
    if request.method == 'POST':
        
        guestbook_name = request.GET.get('guestbook_name',
                DEFAULT_GUESTBOOK_NAME)
        
        greeting = Greeting(parent=guestbook_key(guestbook_name))
        #greeting = Greeting()
        
        #greeting.author = 'oreore5'
        
        #greeting.content = 'testdesuyo5'
        greeting.author = request.POST.get('author')
        greeting.content = request.POST.get('content')
        greeting.put()
        
        #return HttpResponse("Hello, sign_post world. powered by django.")
        return HttpResponseRedirect('/guestbook/')
    
    return HttpResponseRedirect('/guestbook/')

