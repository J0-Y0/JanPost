from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm
from django.views.generic import ListView
from .filter import PostFilterForm
from django.conf import settings
from django.db.models import Count


def globalContext(request):
    context = {
        "category": Category.objects.all(),
        "companyName": settings.COMPANY_NAME,
        # "reportForm": saveReport(request),
    }
    return context


def landingPage(request):
    context = {
        "tags": Post.tags.all()[0:15],
        "posts": Post.newManager.all()[0:2],
        "most_liked_posts": Post.newManager.annotate(
            liked_count=Count("liked")
        ).order_by("-liked_count")[:5],
    }
    return render(request, "blog/landingPage.html", context=context)


def home(request):

    posts = Post.newManager.all()

    # postFilterForm = PostFilterForm(request.GET, queryset=posts)
    # posts = postFilterForm.qs

    context = {
        "posts": posts[:22],
    }

    return render(request, "blog/home.html", context=context)


def postDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    authorsPost = Post.newManager.filter(author=post.author)[:5]
    comments = post.comments.filter(status=True)
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_single", id=2)
    else:
        commentForm = CommentForm()
    context = {
        "post": post,
        "comments": comments,
        "commentForm": commentForm,
        "relatedPost": post.tags.similar_objects()[:5],
        "authorsPost": authorsPost,
    }
    return render(
        request,
        "blog/postDetail.html",
        context=context,
    )


def postsInTag(request, tag):
    posts = Post.newManager.filter(tags__slug__in=[tag])
    context = {
        "posts": posts,
        "tag": tag,
    }
    return render(request, "blog/postsInTag.html", context)


class catList(ListView):
    template_name = "blog/categoryView.html"
    context_object_name = "catList"

    def get_queryset(self):

        content = {
            "cat": self.kwargs["category"],
            "posts": Post.newManager.filter(category__name=self.kwargs["category"]),
        }
        return content


def searchPost(request):
    postSearchForm = PostSearchForm()
    posts = ""
    if request.method == "GET":
        postSearchForm = PostSearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data["searchField"]
            posts = Post.newManager.filter(title__contains=keyword)
    context = {"postSearchForm": postSearchForm, "posts": posts}
    return render(
        request,
    )
