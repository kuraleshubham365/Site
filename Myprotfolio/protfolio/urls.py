from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('skills', views.skills, name="skills"),
    path('about', views.about, name='about'),
    #path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    #path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    #path('login/', views.loginPage, name='login'),
    #path('logout/', views.logoutUser, name='logout'),
    #path('register/', views.registerPage, name='register'),
]
