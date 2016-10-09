from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from himsog.models import Content


class HomePage(View):
    
    def get (self, request):

        return render(request, 'home.html', {'categories':categories})

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
