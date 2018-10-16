from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404,redirect

from .forms import CommentForm
from .models import Comments


# @login_required #(login_url='/login/') #LOGIN_URL = '/login/'
def comment_delete(request, id):

   

    obj = Comments.objects.filter(id=id)
    # render(request, "confirm_delete.html", context)
    print(id1)
    # print(user.id)
    print(request.user.id)
    obj.delete()
    url='/'+ id1
    messages.success(request, "This has been deleted.")
    return redirect(url)
    # obj = CommentFormmment.objects.get(id=id)
    # try:
    #     obj = Comment.objects.get(id=id)
    # except:
    #     raise Http404

    # if obj.user != request.user:
    #     #messages.success(request, "You do not have permission to view this.")
    #     #raise Http404
    #     reponse = HttpResponse("You do not have permission to do this.")
    #     reponse.status_code = 403
    #     return reponse
    #     #return render(request, "confirm_delete.html", context, status_code=403)

    # if request.method == "POST":
    #     parent_obj_url = obj.content_object.get_absolute_url()
    #     obj.delete()
    #     messages.success(request, "This has been deleted.")
    #     return HttpResponseRedirect(parent_obj_url)
    # context = {
    #     "object": obj
    # }
    # return render(request, "confirm_delete.html", context)