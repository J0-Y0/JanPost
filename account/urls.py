from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('activate/<str:uidb64>/<str:token>',views.activate_account,name='activate'),

    path('profile/',views.user_profile,name='profile'),
]

# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        