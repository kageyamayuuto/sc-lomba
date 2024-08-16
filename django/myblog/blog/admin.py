from django.contrib import admin

# import function from models
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
# Register your models here.
