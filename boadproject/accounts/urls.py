from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns =[
    path('register/', views.SignUpView.as_view(), name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),  name='login' ), 
    path('password/', views.B.as_view(),  name='password'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout' ), 
    path('password/done/', views.A.as_view(), name = 'password_reset_done'),
    path(r'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'), 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_done.html"), name='password_complete'), 
]