from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
  ARTICLE_CATEGORY = (
    ('sports', 'sports'),
    ('political', 'political'),
    ('music', 'music'),
    ('finance', 'finance')
  )
  type = models.CharField(max_length=50, choices=ARTICLE_CATEGORY, default='sports')

  def __str__(self):
    return self.type

class News(models.Model):
  title = models.CharField(max_length=200)
  content = models.CharField(max_length=2000)
  pub_date = models.DateTimeField('date published')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

