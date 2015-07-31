# -*- coding:utf-8 -*-
from django.template import Context, loader
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    
    """
    c = Context()
    t = loader.get_template('hello/index.html')
    return HttpResponse("Hello, world. powered by django.")
    return HttpResponse(t.render(c))
    """
    
    template_values = Context({
           'message': 'one more hello!',
            })

    #return render_to_response('hello/index.html')
    return HttpResponse(loader.get_template('hello/index.html').render(template_values))


