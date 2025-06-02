from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# tablename: Article
class Article(models.Model):
    title = models.CharField(max_length=200) # title of the article
    body = models.TextField() # body of the article
    published_date = models.DateTimeField(auto_now_add=True) # date when the article was published
    author = models.ForeignKey(User, on_delete=models.CASCADE) # author of the article
    is_draft = models.BooleanField(default=False) # whether the article is a draft or not
    featured_image = models.ImageField(upload_to='article_images/', blank=True, null=True) 
    # featured image for the article

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={'pk': self.pk})