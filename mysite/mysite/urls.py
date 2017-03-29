from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.index',name ="index"),
    url(r'^zhuce/$','blog.views.zhuce',name="zhuce"),
    url(r'^denglu/$','blog.views.denglu',name="denglu"),
    url(r'blog/(\d+)$','blog.views.blog'),
    url(r'^acc_regist$','blog.views.acc_regist',name="acc_regist"),
    url(r'^acc_login$','blog.views.acc_login',name="acc_login"),
    url(r'^logout$','blog.views.logout',name="logout"),
)
