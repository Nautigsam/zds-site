# coding: utf-8

from django import template

from lbp.forum.models import Category as fCategory
from lbp.project.models import Category as pCategory

register = template.Library()


@register.filter('top_categories')
def top_categories(user):
    categories = fCategory.objects.all().order_by('position')
    
    return categories

@register.filter('top_categories_news')
def top_categories_news(user):
    categories = pCategory.objects.all()
    liste=[]
    for c in categories :
        if c.get_news_count()>0:
            liste.append(c)
    
    return liste
    