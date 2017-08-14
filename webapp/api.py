# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse ,JsonResponse
from django.template import loader
from bson.json_util import dumps
import helper as db

def news(request):
    if request.method == 'GET':
        count = int(request.GET['count'])
        result = db.api_getnews(count)
        data=dumps(result)
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse({"data":"bad request"})


