from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Model, DateTimeField, CharField, TextField, ForeignKey, CASCADE, FileField, EmailField


class BaseModel(Model):
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)


class User(AbstractBaseUser):
    username = CharField(max_length=255)
    password = CharField(max_length=255)
    email = EmailField(max_length=255)


class Posts(BaseModel):
    title = CharField(max_length=255)
    description = TextField()
    author = ForeignKey('auth.User', CASCADE)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = ForeignKey('app.Posts', CASCADE)
    text = CharField(max_length=255)
    file = FileField(upload_to='comment/file/', null=True, blank=True)
    author = ForeignKey('auth.User', CASCADE)
