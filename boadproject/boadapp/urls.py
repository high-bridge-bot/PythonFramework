from django.urls import path
from . import views

app_name = 'boadapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('success/', views.SuccessView.as_view(), name='index_login'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
