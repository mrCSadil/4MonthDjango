from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_friend/', views.about_my_friend, name='about_my_friend'),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/<int:id>/', views.post_detail_view, name='post_detail'),
    path("posts/create/", views.post_create_view, name='post_create_view'),
]
