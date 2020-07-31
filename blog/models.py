from django.db import models
#from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=70)
    content=models.TextField()
    date_posted=models.DateTimeField(default=datetime.datetime.today)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'post {self.title}'
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

