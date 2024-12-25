from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('add/', views.article_add, name='add'),
    path('category/<str:category>/', views.category_article, name='category'),
    path('detail/<int:article_id>/', views.detail_article, name='detail'),
]
