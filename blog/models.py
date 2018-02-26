from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    #文章的分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        # 为了使显示的数据更人性化，所以我们这里使用了__str__方法，这样解释器显示的内容将会是 __str__ 方法返回的内容
        #这里会使数据显示出文章的名字
class Tag(models.Model):
    #文章的标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    #文章
    title = models.CharField(max_length=70)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True) #文章的摘要
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User) #文章的作者

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 自定义 get_absolute_url 方法
        return reverse('blog:detail', kwargs={'pk': self.pk})
        #reverse函数会去解析detail函数对应的url，也就是 post/(?P<pk>[0-9]+)/ 这个正则表达式，而正则表达式部分会被后面传入的参数 pk 替换，所以，如果 Post 的 id（或者 pk，这里 pk 和 id 是等价的） 是 255 的话，那么 get_absolute_url 函数返回的就是 /post/255/ ，这样 Post 自己就生成了自己的 URL。