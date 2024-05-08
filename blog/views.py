from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm, ReportForm
from django.views.generic import ListView
from .filter import PostFilterForm
from django.conf import settings


def landingPage(request):
    return render(request, "blog/landingPage.html")


def home(request):
    reportForm = ReportForm()
    if request.method == "POST":
        reportForm = ReportForm(request.POST)
        if reportForm.is_valid():
            report = reportForm.save(commit=False)

            report.save()

    posts = Post.newManager.all()
    # if request.method == 'GET':
    #     postSearchForm = PostSearchForm(request.GET)
    #     if postSearchForm.is_valid():
    #         keyword = postSearchForm.cleaned_data['searchField']
    #         posts = Post.newManager.filter(title__contains = keyword )

    postFilterForm = PostFilterForm(request.GET, queryset=posts)
    posts = postFilterForm.qs

    context = {
        "reportForm": reportForm,
        "postFilterForm": postFilterForm,
        "posts": posts,
    }

    return render(request, "blog/index.html", context=context)


def post_single(request, id):
    post = get_object_or_404(Post, id=id)
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
    }
    return render(
        request,
        "blog/single.html",
        context=context,
    )


class catList(ListView):
    template_name = "blog/categoryView.html"
    context_object_name = "catList"

    def get_queryset(self):

        content = {
            "cat": self.kwargs["category"],
            "posts": Post.newManager.filter(category__name=self.kwargs["category"]),
        }
        return content


def globalContext(request):
    context = {"category": Category.objects.all(), "companyName": settings.COMPANY_NAME}
    return context


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
