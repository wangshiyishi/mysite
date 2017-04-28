# coding:utf-8
from django.shortcuts import render, render_to_response
from .models import *
from django.http import HttpResponseRedirect
from models import Comment
# Create your views here.


def index(req):
    username = req.COOKIES.get('username', "")
    blogs = Blog.objects.all()
    return render_to_response("index.html",
                              {"blogs": blogs,
                               'username': username})


def zhuce(self):
    return render_to_response("zhuce.html")


def denglu(self):
    return render_to_response("denglu.html")


def blog(self, blog_id):
    blogs = Blog.objects.all().get(id=blog_id)
    return render_to_response('blog.html', {"blog": blogs})


def acc_regist(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')

    if User.objects.all().filter(username=username):
        return render_to_response("zhuce.html", {'error': '用户名已存在'})
    else:
        if password == repassword:
            User.objects.create(username=username, password=password)
            username = request.COOKIES.get('username', "")
            blogs = Blog.objects.all()
            return render_to_response("index.html", {"blogs": blogs, 'username': username})
        else:
            return render_to_response("zhuce.html", {'error': '恭喜你活下来了'})


def acc_login(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    if User.objects.all().filter(username=username):
        user = User.objects.all().get(username=username)
        if password == password:
            response = HttpResponseRedirect('/')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return render_to_response("denglu.html", {'error': '恭喜你活下来了'})

    else:
        return render_to_response("denglu.html", {'error': '去死哦'})


def logout(req):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    return response


def blog(request):
    comments = Comment.objects.all()
    return render(request,
                  'blog.html',
                  {'comments': comments})


def sub_comment(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    username = request.COOKIES.get('username', "")
    user = User.objects.get(username=usernae)
    comment = request.POST.get('comments')
    Comment.objects.create(comments=comment, author=user, blog=blog)
    return HttpResponseRedirect('/')


def delete_comment(request, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return HttpResponse('/')


def update_comment(request, comment_id):
    comment = request.POST.get('comments')
    Comment.objects.filter(id=comment_id).update(Comment=comment)
