from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    text = models.CharField(max_length=100, unique=True)
    rating = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField()
    rating = models.IntegerField(default=0)

class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(Profile, models.SET_NULL, null = True)
    rating = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank = True)

class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile, models.SET_NULL, null = True)
    is_correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    to_question = models.ForeignKey(Question, models.CASCADE)
