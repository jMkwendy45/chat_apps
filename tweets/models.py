from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    # image = models.FieldFile(upload_to ='images/',blank=True,null=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)




