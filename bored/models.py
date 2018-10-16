from django.db import models
from django.core.urlresolvers import reverse
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from comments.models import Comments
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class Contents(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	user_name  = models.CharField(max_length=120)
	title = models.CharField(max_length=120)
	

	details = models.TextField(default='',blank=True)
	#Discriptions = RichTextField(null=True,blank=True)
	Discriptions = models.TextField(default='',blank=True)
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse("bored:detail",kwargs={"id":self.id})
	
	
	
	@property
	def comments(self):
		instance = self
		qs = Comments.objects.filter_by_instance(instance)
		return qs
	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type
	class Meta():
		ordering = ["-timestamp"]