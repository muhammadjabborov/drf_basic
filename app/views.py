from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from app.serializers import PostSerializers, CommentSerializer

from app.models import Posts, Comment


class PostListApiView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class PostAddApiView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class PostDestroyAPIView(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    lookup_url_kwarg = 'pk'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    lookup_url_kwarg = 'pk'


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
