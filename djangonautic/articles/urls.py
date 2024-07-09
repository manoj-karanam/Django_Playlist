from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='list'),
    path('<slug:slug>/', views.article_detail, name ='detail'),

# This uses the path function and specifies that the slug parameter should be matched using Django's 
# built-in slug converter. The slug converter matches any slug string containing letters, numbers, underscores, and hyphens

]