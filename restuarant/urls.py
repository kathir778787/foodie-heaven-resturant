from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.user_login, name='login'),  
    path('register/', views.register, name='register'),
    path('policy/', views.policy, name='policy'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('dishes/', views.dishes, name='dishes'),
    path('ourdishes/', views.ourdishes, name='ourdishes'),
    path('reservation/', views.reservation, name='reservation'),
    path('index/', views.index, name='index'),
     path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
     path('logout/', views.logout_view, name='logout'),


    # Admin routes (organized under admin/)
    path('admin1/contact/', views.admin_contact, name='admin_contact'),
    path('admin1/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin1/dishes/', views.admin_dishes, name='admin_dishes'),
    path('admin1/login/', views.admin_login, name='admin_login'),
    path('admin1/reservation/', views.admin_reservation, name='admin_reservation'),
]
