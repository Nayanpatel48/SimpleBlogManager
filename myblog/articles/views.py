from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'  # default: <app>/<model>_list.html
    context_object_name = 'articles'
    ordering = ['-published_date']

    def get_queryset(self):
        # Show only non-draft articles
        return Article.objects.filter(is_draft=False).order_by('-published_date')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'  # default: <app>/<model>_detail.html

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body', 'is_draft', 'featured_image']  # you can choose to let authors set draft status
    template_name = 'articles/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'body', 'is_draft', 'featured_image' ]  
    # you can choose to let authors set draft status
    template_name = 'articles/article_form.html'

    def form_valid(self, form):
        # Ensure author remains same
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Only the author can update
        article = self.get_object()
        return self.request.user == article.author

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author