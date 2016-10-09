from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse

from himsog.models import Category


class CategoryView(View):
    
    def get (self, request):
        category_list = Category.objects.values_list('name', flat=True)

        response = JsonResponse({'data' : list(category_list)})

        return response
