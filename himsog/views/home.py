from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

from himsog.models import Category
from himsog.models import Content


class Landing(View):

    def get(self, request):
        context_dict = dict()
        return render(request, 'landing.html') 


class Home(View):

    def get(self, request):
        # context_dict = dict()

        # if category_slug:
        #     cat = Category.objects.filter(slug_name=category_slug)
        #     context_dict['contents'] = Content.objects.filter(category=cat)
        #     context_dict['active'] = cat[0].name
        # else:
        #     context_dict['contents'] = Content.objects.all()
        #     context_dict['active'] = 'All'

        return render(request, 'home.html') 
