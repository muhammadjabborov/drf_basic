from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from app.serializers import PostSerializers

from app.models import Posts


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


