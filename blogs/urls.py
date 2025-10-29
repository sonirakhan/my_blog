from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('blogs-detail/<slug:post_slug>/',views.post_detail,name='post_detail'),
]
