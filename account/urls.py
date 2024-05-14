from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import PwdResetRequestForm, PwdResetForm

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("signup/", views.user_signup, name="signup"),
    path("activate/<str:uidb64>/<str:token>", views.activate_account, name="activate"),
    # Password reset| using django default class view
    path(
        "password_reset_request/",
        auth_views.PasswordResetView.as_view(
            form_class=PwdResetRequestForm,
            html_email_template_name="registration/password_reset_email.html",
        ),
        name="pwdreset_request",
    ),
    path(
        "password_reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(form_class=PwdResetForm),
        name="pwdreset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/done",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("profile/", views.user_profile, name="profile"),
    path("activity", views.activity, name="activity"),
]

# htmx urls
htmxUrl = [
    path("savePost/<int:pid>", views.savePost, name="savePost"),
    path("likePost/<int:pid>", views.likePost, name="likePost"),
    path("dislikePost/<int:pid>", views.dislikePost, name="dislikePost"),
    path("commentPost/<int:pid>", views.commentPost, name="commentPost"),
]

urlpatterns += htmxUrl

# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
