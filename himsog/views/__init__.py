from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from himsog.models import Category
from himsog.models import Content

class HomePage(View):
    
    def get (self, request):

        return render(request, 'home.html')

class ContentPage(View):
    '''
    @class ContentPage
    @brief View class for Content Page
    '''
    
    def get (self, request, id):
        '''
        @fn get
        @brief Handles HTTP GET request
        @param[in] request - HTTP request
        @param[in] id - Content ID
        '''

        content = get_object_or_404(Content,
                                    pk=id)

        return render(request, 'content.html', {'content':content})

class CategoryContentListPage(View):

	def get(self, request, category_slug=None):

		context = dict()
		cat_slug = category_slug

		cat = Category.objects.get(slug_name=cat_slug)
		contents = Content.objects.filter(category=cat)

		context['contents'] = contents
		return render(request, 'category_content_list.html', context) 
