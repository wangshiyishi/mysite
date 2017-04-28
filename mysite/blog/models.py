#coding:utf-8
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length= 10,verbose_name='用户名')
    password = models.CharField(max_length=240,verbose_name='密码')
    created_at = models.DateTimeField(auto_now_add= True,verbose_name='建立时间')

class Blog(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    created_at = models.DateTimeField(auto_now_add= True,verbose_name='建立时间')
   # photo = models.ImageField(upload_to= "static/Blog_img",blank= True,null=True,verbose_name='图片')
    ccontent = models.TextField(verbose_name='内容')


class Comments(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='博客')
    author = models.ForeignKey(User,verbose_name='作者')
    comments = models.CharField(max_length= '350',verbose_name='评论')
    created_at= models.DateTimeField(auto_now_add= True,verbose_name='创建时间')


