from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.CharField(max_length=280)
    image = models.ImageField(upload_to='images/', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    fields = ('title','post_text','pub_date',)
    def save_model(self, request, instanceli, form, change):
        obj.author = request.user
        obj.save()