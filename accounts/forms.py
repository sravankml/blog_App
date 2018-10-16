from django import forms

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
User = get_user_model()
from django.contrib.auth.forms  import UserChangeForm
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
    	username = self.cleaned_data.get("username")
    	password=self.cleaned_data.get("password")
    	
    	if username and password:
	    	user = authenticate(username=username,password=password)
	    	if not user:
	    		raise forms.ValidationError("This user does not exist")
	    	if not user.check_password(password):
	    		raise forms.ValidationError("Incorrect password")
	    	if not user.is_active:
	    		raise forms.ValidationError("This user is not active")
	    	return super(UserLoginForm,self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Confirm Email')
    email2 = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)
    # staff = forms.BooleanField(default=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email2',
            'email',
            'password'
        ]
    def clean_email(self):
    	email = self.cleaned_data.get('email')
    	email2 = self.cleaned_data.get('email2')
    	if email != email2:
    		raise forms.ValidationError("Email must match")
    	return email
    # @property
    # def is_staff(self):
    #     return self.staff
    # 
class EditUserProfile(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]