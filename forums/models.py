from django.db import models

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=280)
    pub_date = models.DateTimeField('date published')
