from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('<int:id>',views.post_single,name="post_single"),
    # path('<str:category>',views.catList.as_view(),name = 'categoryView')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        