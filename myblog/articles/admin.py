from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_draft')
    search_fields = ('title', 'body')
    list_filter = ('is_draft', 'published_date', 'author')
    ordering = ('-published_date',)