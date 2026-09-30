from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.home, name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('post/<int:post_id>/',views.post_details, name='post_details'),
    path('user/<str:username>/',views.user_profile,name='post_details'),

    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year, name='article_by_year'),

    path ('article/<int:year>/<int:month>',views.article_details, name='article_details'),

    path('renderHtml/',views.post_list,name='post_list'),

    path('blog-details/', views.blog_details, name='blog-details'),

    path('homeview/', views.home_view, name='home_view')
    
]