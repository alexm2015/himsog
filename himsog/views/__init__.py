from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import View

from himsog.models import Category
from himsog.models import Content


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
        image_count = content.images.count()

        context = {'content': content,
                   'image_count': range(image_count)}

        return render(request, 'content.html', context)
