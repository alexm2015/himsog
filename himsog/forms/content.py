from django import forms
from django.forms.formsets import BaseFormSet
from django.forms.formsets import formset_factory


# from tinymce.widgets import TinyMCE
#
# from himsog.models import Category
# class ContentForm(forms.Form):
#
#     category = forms.ModelChoiceField(queryset=Category.objects.all())
#     title = forms.CharField()
#     description = forms.CharField(widget=TinyMCE())
#     images = forms.ImageField()
class OverviewForm(forms.Form):

    title = forms.CharField()
    about = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()

class MenuForm(forms.Form):

    item = forms.CharField()
    description = forms.CharField()
    price = forms.CharField()

class PhotoForm(forms.Form):

    file = forms.ImageField()
    name = forms.CharField(widget=forms.HiddenInput)
    url = forms.CharField(widget=forms.HiddenInput)

MenuFormSet = formset_factory(form=MenuForm, formset=BaseFormSet)
PhotoFormSet = formset_factory(form=PhotoForm, formset=BaseFormSet)

