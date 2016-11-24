from django import forms
from himsog.models import Category

class ContentForm(forms.Form):

    category = forms.ModelChoiceField(queryset=Category.objects.all())
    title = forms.CharField()
    description = forms.CharField(widget=forms.widgets.Textarea)
    images = forms.ImageField()

