from django.contrib import admin
from .models import User,Blog,Comments
# Register your models here.
class User_Admin(admin.ModelAdmin):
    list_display = ('username','password','created_at',)

class Blog_Admin(admin.ModelAdmin):
    list_display = ('title','created_at',)

class Comments_Admin(admin.ModelAdmin):
    list_display = ('blog','created_at','author',)

admin.site.register(User,User_Admin)
admin.site.register(Blog,Blog_Admin)
admin.site.register(Comments,Comments_Admin)