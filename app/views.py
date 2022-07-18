from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from app.models import Posts, Comment
from app.serializers import PostSerializers, CommentSerializers

from app.models import Posts, Comment


# POST CRUD


class PostAPIViewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class PostListApiView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    pagination_class = PostAPIViewPagination


class PostAddApiView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class PostDestroyAPIView(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    lookup_url_kwarg = 'id'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    lookup_url_kwarg = 'id'


class PostModelViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    pagination_class = PostAPIViewPagination


# COMMENT CRUD

class CommentAPIViewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class CommentLIstAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    pagination_class = CommentAPIViewPagination


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    lookup_url_kwarg = 'id'


class CommentDestroyAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    lookup_url_kwarg = 'id'


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    pagination_class = CommentAPIViewPagination
