from django.contrib import admin
from django.urls import path

from app.views import PostListApiView, PostAddApiView, PostDestroyAPIView, PostUpdateAPIView

urlpatterns = [
    path('post-list', PostListApiView.as_view(), name='post-list'),
    path('post-add', PostAddApiView.as_view(), name='post-add'),
    path('post-delete/<int:pk>', PostDestroyAPIView.as_view(), name='post-delete'),
    path('post-update/<int:pk>', PostUpdateAPIView.as_view(), name='post-update'),
]
