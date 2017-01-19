from django import forms
from tinymce.widgets import TinyMCE

from himsog.models import Category


class ContentForm(forms.Form):

    category = forms.ModelChoiceField(queryset=Category.objects.all())
    title = forms.CharField()
    description = forms.CharField(widget=TinyMCE())
    images = forms.ImageField()

