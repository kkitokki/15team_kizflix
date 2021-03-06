# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from contents.models import PostModel

# Create your models here.


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    nickname = models.CharField(max_length=256, null=False)
    password2 = models.CharField(max_length=256, null=False)

class UserLikes(models.Model):
    class Meta:
        db_table = "user_likes"
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_id')
    post_id = models.ForeignKey(PostModel, on_delete=models.CASCADE, db_column='post_id')
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfiles(models.Model):
    class Meta:
        db_table = "user_profile"
    user = models.OneToOneField(UserModel, related_name="profile", on_delete=models.CASCADE)
    pf_image = models.ImageField(upload_to='pf_image/', default='octonut.png')

