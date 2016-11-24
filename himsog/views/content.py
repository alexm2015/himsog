from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from himsog.forms.content import ContentForm
from himsog.models import Content


class ContentView(View):
    """
    """

    context = {}

    def get(self, request, content_id):
        """
        """

        content = get_object_or_404(Content, pk=content_id)

        self.context['content'] = content
        self.context['image_count'] = range(content.images.count())

        return render(request,
                      'content.html',
                      self.context)


class ContentAddView(View):
    """
    """

    context = {}

    def get(self, request):
        """
        """

        content_form = ContentForm()
        self.context['form'] = content_form

        return render(request,
                      'content_add.html',
                      self.context)

    def post(self, request):
        """
        """

        content_form = ContentForm(request.POST)

        if not content_form.is_valid():
            # return error
            pass

        content_form.clean()
        content = Content()
        content.category = content_form.cleaned_data.get('category')
        content.title = content_form.cleaned_data.get('title')
        content.description = content_form.cleaned_data.get('description')
        # TODO: add images

        content.save()

        self.context['content'] = content
        self.context['image_count'] = range(content.images.count())

        return render(request,
                      'content.html',
                      self.context)

class ContentUpdateView(View):
    pass

class ContentDeleteView(View):
    pass
