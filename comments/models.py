from django.db import models
# from bored.models import Contents
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse,HttpResponseRedirect,Http404
# Create your models here.
class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager,self).filter(parent=None)
        return qs
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id= obj_id).filter(parent=None)
        return qs
class Comments(models.Model):

    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent      = models.ForeignKey("self", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    content     = models.TextField()
    objects = CommentManager()

    def __str__(self):
        return str(self.user.username)
    def get_delete_url(self):
        return reverse("comments:delete", kwargs={"id": self.id})
        
    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
    class Meta():
        ordering = ["-timestamp"]