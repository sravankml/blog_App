from django.shortcuts import render,get_object_or_404,redirect
import random
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .forms import ContentForm
from .models import Contents
from django.contrib import messages
from comments.models import Comments
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model,get_user
from comments.forms import CommentForm
from django.contrib.auth.models import User
def HomeView(request):
		quaryset = Contents.objects.all()
		context = {
		"box_num":quaryset
		}
		return render(request,"home.html",context)
class AboutView(TemplateView):
	template_name = 'about.html'
	
class FrontView(TemplateView):
	template_name = 'front.html'
class ProfileView(TemplateView):
	
	template_name = 'profile.html'
	def get(self,request):
		obj=Contents.objects.filter(user_name = request.user)
		print(User.username)
		
		return render(request,"profile.html",{"instance":obj})


def createView(request):
	
	
	
	form = ContentForm(request.POST or None,request.FILES or None,initial={"user_name" : request.user})
	if form.is_valid():
		content_item = form.save(commit=False)
		content_item.save()
		return HttpResponseRedirect('/')
	context = {
		"forms":form
			}
	return render(request,"create_form.html",context)
def post_detail(request,id): #retrieve
	#instance = post.objects.get(id=7)
	
	instance = get_object_or_404(Contents,id=id)
	
	# print(User.username)
	# print(request.user)
	username=str(instance.user_name)
	name = str(request.user)
	print(name)
	print(instance.user_name)
	content_type =ContentType.objects.get_for_model(Contents)
	obj_id = instance.id
	initial_data = {
		"content_type":instance.get_content_type,
		"object_id":instance.id
	}
	form = CommentForm(request.POST or None,initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type=ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get("object_id")
		content_data = form.cleaned_data.get("content")
		new_comment,created = Comments.objects.get_or_create(
									user = request.user,
									content_type = content_type,
									object_id =obj_id,
									content = content_data

													)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

	comments=instance.comments#Comments.objects.filter_by_instance(instance) #(content_type=content_type,object_id=obj_id)

	context ={
	"title":instance.title,
	"instances":instance,
	"comment":comments,
	"comment_form":form,
	"username":username,
	"name" : name
	
	}
	return render(request,"post_detail.html",context)
def editView(request,id=None):	
	if  not request.user.is_authenticated():
		raise Http404
	item = get_object_or_404(Contents,id=id)
	form = ContentForm(request.POST or None,request.FILES or None,instance=item)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/')
		#return HttpResponseRedirect(instance.get_absolute_url())
	context={
	"forms":form
	}
		
	return render(request,"create_form.html",context)
def deleteView(request,id=None):	
	# if  not request.user.is_authenticated():
	# 	raise Http404
	item = get_object_or_404(Contents,id=id)
	item.delete()
	return HttpResponseRedirect('/')

def profile_detail(request,id): #retrieve
	#instance = post.objects.get(id=7)
	
	instance = get_object_or_404(Contents,id=id)
	
	# print(User.username)
	# print(request.user)
	username=str(instance.user_name)
	name = str(request.user)
	print(name)
	print(instance.user_name)
	content_type =ContentType.objects.get_for_model(Contents)
	obj_id = instance.id
	initial_data = {
		"content_type":instance.get_content_type,
		"object_id":instance.id
	}
	form = CommentForm(request.POST or None,initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type=ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get("object_id")
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()
		new_comment,created = Comments.objects.get_or_create(
									user = request.user,
									content_type = content_type,
									object_id =obj_id,
									content = content_data,
									parent = parent_obj

													)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

	comments=instance.comments#Comments.objects.filter_by_instance(instance) #(content_type=content_type,object_id=obj_id)

	context ={
	"title":instance.title,
	"instances":instance,
	"comment":comments,
	"comment_form":form,
	"username":username,
	"name" : name
	
	}
	return render(request,"about.html",context)
	# def post(self,request,*args,**kwargs):
	# 	context={}
	# 	return render(request,'profile.html',context)
	# def put(self,request,*args,**kwargs):
	# 	context={}
	# 	return render(request,'profile.html',context)