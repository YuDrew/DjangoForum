from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

class Post(models.Model):
    title = models.CharField(max_length=70)
    post_text = models.CharField(max_length=280)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    fields = ('title','post_text','pub_date',)
    def save_model(self, request, instanceli, form, change):
        obj.author = request.user
        obj.save()