from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import PostListApiView, PostAddApiView, PostDestroyAPIView, PostUpdateAPIView, \
    CommentLIstAPIView, CommentCreateAPIView, CommentUpdateAPIView, CommentDestroyAPIView, CommentModelViewSet, \
    PostModelViewSet

router_comment = DefaultRouter()
router_comment.register(r'comment', CommentModelViewSet, 'comment')

router_post = DefaultRouter()
router_post.register(r'post', PostModelViewSet, 'post')

'''
comment-list        comment/    GET
comment-add         comment/    POST
comment-retrieve    comment/id  GET
comment-update      comment/id  PATCH, PUT
comment-destroy     comment/id  DELETE

comment/4

'''
urlpatterns = [
    path('', include(router_comment.urls)),
    path('', include(router_post.urls)),

    # path('post-list/', PostListApiView.as_view(), name='post-list'),
    # path('post-add/', PostAddApiView.as_view(), name='post-add'),
    # path('post-delete/<int:id>/', PostDestroyAPIView.as_view(), name='post-delete'),
    # path('post-update/<int:id>/', PostUpdateAPIView.as_view(), name='post-update'),

    # path('comment-list/',CommentLIstAPIView.as_view(),name='comment-list'),
    # path('comment-add/',CommentCreateAPIView.as_view(),name='comment-add'),
    # path('comment-update/<int:id>',CommentUpdateAPIView.as_view(),name='comment-update'),
    # path('comment-delete/<int:id>', CommentDestroyAPIView.as_view(), name='comment-delete'),
]
