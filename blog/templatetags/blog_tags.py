from ..models import Post,Category
from django import template

register = template.Library()

@register.simple_tag #记得加上这个
def get_recent_posts(num=5):
    # 最新文章模板标签
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
    # 归档模板标签
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 分类模板标签
    return Category.objects.all()