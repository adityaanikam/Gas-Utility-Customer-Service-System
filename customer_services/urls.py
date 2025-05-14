from django.urls import path
from . import views

app_name = 'customer_services'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_service_request, name='create_request'),
    path('request/<int:pk>/', views.service_request_detail, name='service_request_detail'),
    path('request/<int:pk>/update/', views.update_service_request, name='update_request'),
    path('profile/', views.profile, name='profile'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
    path('register/', views.register, name='register'),
] 