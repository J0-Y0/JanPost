from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),

    path('signup/',views.user_signup,name='signup'),
    path('activate/<str:uidb64>/<str:token>',views.activate_account,name='activate'),

    path('reset_request/',views.password_reset_Request,name='reset_request'),
    path('reset/<uidb64>/<token>',views.reset_account,
        name='reset'),    
    

    path('profile/',views.user_profile,name='profile'),
]

# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        