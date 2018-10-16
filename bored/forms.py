from django.forms import ModelForm
from .models import Contents
from django import forms
class ContentForm(ModelForm):
	user_name = forms.CharField(widget=forms.HiddenInput)
	class Meta:
		model = Contents
		fields = ["title","details","Discriptions","user_name"]
		