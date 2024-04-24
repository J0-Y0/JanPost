from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import CommentForm

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
