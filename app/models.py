from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count

class TagManager(models.Manager):
    def get_hot_tags(self):
        return self.annotate(q_count=Count('questions')).order_by('-q_count')[:10]

class Tag(models.Model):
    text = models.CharField(max_length=100, unique=True)
    rating = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    # avatar = models.ImageField(default='static/img/1.jpg')
    rating = models.IntegerField(default=0)

class QuestionManager(models.Manager):
    def get_hot_questions(self):
        return self.order_by('-rating')[:40]

    def get_some_questions(self, count=40):
        return self.order_by('-date')[:count]

    def get_question_with_tag(self, tag_id):
        return self.filter(tags__pk=tag_id)

class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(Profile, models.SET_NULL, null = True)
    rating = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank = True)
    date = models.DateField(default=timezone.now)

class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile, models.SET_NULL, null = True)
    is_correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    to_question = models.ForeignKey(Question, models.CASCADE)
    date = models.DateField(default=timezone.now)

class Like(models.Model):
    user = models.ForeignKey(Profile, models.CASCADE, )
    like = models.BooleanField(blank=True, default=False)