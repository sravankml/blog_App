
from django import forms


from .models import Comments
class CommentForm(forms.Form):
		fields = ["content"]
		content_type = forms.CharField(widget=forms.HiddenInput)
		object_id = forms.IntegerField(widget=forms.HiddenInput)
    	#parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
		content = forms.CharField(widget=forms.Textarea,label=" ")