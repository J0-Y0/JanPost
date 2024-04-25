from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category
from .forms import CommentForm
from django.views.generic import ListView

def home(request):
    context = {'posts':Post.newManager.all()}
    return render(request, 'index.html',context = context)
def post_single(request,id):
    post  = get_object_or_404(Post,id = id)
    comments = post.comments.filter(status  =True)
    if request.method == 'POST':
        commentForm =  CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit = False)
            comment.post = post
            comment.save()
            commentForm =  CommentForm()
    else:
        commentForm =  CommentForm()
    context = {'post':post,
               "comments":comments,
               'commentForm':commentForm,}
    return render(request, 'single.html',context = context,)
class catList(ListView):
    template_name = 'categoryView.html'
    context_object_name = 'catList'
    def get_queryset(self):
      
        content = {
            "cat":self.kwargs['category'],
            'posts':Post.newManager.filter(category__name =self.kwargs['category'])
        }
        return content
    
def categorylist(request):
    context = {
        'category': Category.objects.all()
        # 'category': Category.objects.exclude(name = 'Default')
    }
    return context