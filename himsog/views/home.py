from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import View
from django.shortcuts import render

from himsog.models import Category
from himsog.models import Content

import json

import pprint
class Landing(View):

    def get(self, request):
        context_dict = dict()
        return render(request, 'landing.html') 


class Home(View):

    def get(self, request, category_slug=None):
        context_dict = dict()
        return render(request, 'demo.html')   


def get_contents(request):
    response_data = {}

    num_items = None
    last_id = None
    cat_slug = None
    status = 200

    #todo: move constants
    DEFAULT_NUM_CONTENTS = 3

    print('Last ID: {0}.'.format(request.GET['last_id']))
    print('Cat Slug: {0}.'.format(request.GET['cat_slug']))

    result = None
    desc = 'No description.'
    contents = []
    
    if request.method == 'GET':
        num_items = 'num_items' in request.GET and int(request.GET['num_items']) or DEFAULT_NUM_CONTENTS   
        cat_slug = 'cat_slug' in request.GET and request.GET['cat_slug'] or False
        last_id = 'last_id' in request.GET and int(request.GET['last_id']) or False
        
        if cat_slug:
            cat = Category.objects.filter(slug_name=cat_slug)
            if cat:
                if last_id:
                    contents_objs = Content.objects.filter(id__lt=last_id, category=cat).order_by('id').reverse()[:num_items]
                else:  
                    contents_objs = Content.objects.filter(category=cat).order_by('id').reverse()[:num_items]
                #contents = serializers.serialize('json', contents_objs)
                result = "OK"
            else:
                result = "NG"
                description = "Invalid category slug."
        else:
            if last_id:
                contents_objs = Content.objects.filter(id__lt=last_id).order_by('id').reverse()[:num_items]
            else:
                contents_objs = Content.objects.all().order_by('id').reverse()[:num_items]
            #contents = serializers.serialize('json', contents_objs)
        
       
        # pprint.pprint(contents_objs)
        for content in contents_objs:
            content_dic = {}
            content_dic['id'] = content.id
            content_dic['title'] = content.title
            content_dic['description'] = content.description
            content_dic['views'] = content.views
            content_dic['rating'] = content.rating
            print('ID: {0}'.format(content.id))
            contents.append(content_dic)

        #todo, dont include unneededed
        response_data['result'] = result
        response_data['contents'] = contents
        response_data['desc'] = desc
        # pprint.pprint(last_id)
        pprint.pprint(response_data['contents'])
        # pprint.pprint(response_data)
        return JsonResponse(response_data, status=status)
    else:
        return HttpResponse(status=400)