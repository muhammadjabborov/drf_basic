from rest_framework.serializers import ModelSerializer

from app.models import Posts, Comment


class PostSerializers(ModelSerializer):
    class Meta:
        model = Posts
        exclude = ()


class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ()
