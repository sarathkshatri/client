from django.conf.urls import url
from django.urls import path
#from . import views
from .views import SignUpView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
     name='password_reset_complete'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),


    url(r'^password/$', views.change_password, name='change_password'),
]
