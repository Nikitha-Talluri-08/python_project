from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='views.login'),
    path('signup/', views.signup, name='views.signup'),
    path('eligibility/', views.eligibility, name='views.eligibility'),
    path('faqs/', views.faqs, name='views.faqs'),
    path('instructions/', views.instructions, name='views.instructions'),
    path('payment/', views.payment, name='views.payment'),
    path('apply/', views.apply, name='views.apply'),
    path('regular/', views.regular, name='views.regular'),
    path('regular/r2/', views.r2, name='views.r2'),
    path('regular/r2/r3', views.r3, name='views.r3'),
    path('regular/r2/r4', views.r4, name='views.r4'),
    path('regular/r2/r5', views.r5, name='views.r5'),
    path('regular/r2/r6', views.r6, name='views.r6'),
    path('regular/r2/r7', views.r7, name='views.r7'),
    path('i1/', views.i1, name='views.i1'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('apply-for-visa/', apply_for_visa, name='apply_for_visa'),

]