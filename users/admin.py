from django.contrib import admin
from .models import UserModel, UserLikes

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserLikes)
