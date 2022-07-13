from rest_framework.serializers import ModelSerializer

from app.models import Posts


class PostSerializers(ModelSerializer):
    class Meta:
        model = Posts
        exclude = ()
