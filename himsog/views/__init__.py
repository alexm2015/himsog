from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

from himsog.models import Category
from himsog.models import Content
class HomePage(View):
    
    def get (self, request):

        categories = Category.objects.all()

        return render(request, 'home.html', {'categories':categories})

class CategoryContentListPage(View):

	def get(self, request, category_slug=None):

		context = dict()
		cat_slug = category_slug

		cat = Category.objects.get(slug_name=cat_slug)
		contents = Content.objects.filter(category=cat)

		context['contents'] = contents
		return render(request, 'category_content_list.html', context) 
