from django.urls import path
from .import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('addcar/',views.add_car, name='addcar'),
    path('carlist/', views.car_list, name='carlist'),
    path('editcar/<int:car_id>/', views.edit_car, name='editcar'),
    path('deletecar/<int:car_id>/', views.delete_car, name='deletecar'),

]
