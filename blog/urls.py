from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('<int:id>',views.post_single,name="post_single"),
    
]
