from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', views.ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article-delete'),
]