from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path("home", views.home, name="home"),
    path("<slug:slug>", views.postDetail, name="postDetail"),
    path("tags/<slug:tag>", views.postsInTag, name="postsInTag"),
    # path('<str:category>',views.catList.as_view(),name = 'categoryView')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
