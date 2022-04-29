from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomePageView.as_view(),name='home_page'),
    path('about/',views.AboutPageView.as_view(),name='about_page'),
    path('post_create/',views.PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
] 