# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.

import helper as db
def index(request):
    template=loader.get_template('index.html')
    result = db.getnews(15)

    news_list =[]
    for new in result:
        news_list.append(new)
    context = {"news_list": news_list, }
    return HttpResponse(template.render(context, request))

def new_detail(request):
    if request.method == "GET":
        title = request.GET['title']
        template = loader.get_template('news.html')
        result = db.newByTitle(title)
        context={"new_detail": result}
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("error")

@csrf_exempt
def login(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            pwd = request.POST['pwd']
            print email,pwd
            #template = loader.get_template('index.html')
            return HttpResponseRedirect("/webapp/")
        else:
            template = loader.get_template('login.html')
            return HttpResponse(template.render({}, request))
    except Exception as e:
        pass


@csrf_exempt
def topic(request):
    try:
        if request.method == 'POST':
            vertor = request.POST['email']
            pwd = request.POST['pwd']
            print email, pwd
            # template = loader.get_template('index.html')
            return HttpResponseRedirect("/webapp/")
        else:
            template = loader.get_template('login.html')
            return HttpResponse(template.render({}, request))
    except Exception as e:
        pass
