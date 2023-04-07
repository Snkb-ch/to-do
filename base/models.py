from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255, null=True, unique=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(default="avatar.svg", blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

    pass

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    Deadline = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=0, null=True, blank=True)



    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'



