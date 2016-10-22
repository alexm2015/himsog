from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

from himsog.models import Category
from himsog.models import Content


class Home(View):

    def get(self, request, category_slug=None):
        context_dict = dict()

        if category_slug:
            cat = Category.objects.filter(slug_name=category_slug)
            context_dict['contents'] = Content.objects.filter(category=cat)
        else:
            context_dict['contents'] = Content.objects.all()
        
        return render(request, 'home.html', context_dict) 
