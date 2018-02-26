from django.conf.urls import url
from .import views

app_name = 'blog' #告诉了 Django 这个 URL 模块是属于 blog 应用的，因此 Django 能够顺利地找到 blog 应用下 name 为 detail 的视图函数
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #这个正则表达式的意思是：以 post/ 开头，后跟一个至少一位数的数字，并且以 / 符号结尾，如 post/1/、 post/255/ 等都是符合规则的，[0-9]+ 表示一位或者多位数。
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),

]