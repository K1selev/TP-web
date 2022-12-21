from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class ProfileManager(models.Manager):
    def best(self):
        return self.order_by('-rating')[:5]
    
    def is_exist(self, name, email):
        return User.objects.filter(username=name).count()

class Profile(models.Model):
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(
        upload_to='static/img/avatars', default='static/img/avatar_1.png'
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

class TagManager(models.Manager):
    def popular(self):
        return self.order_by('-references_num')[:10]
    
    def create_from_list(self, tags):
        for n in tags:
            if not self.filter(name=n).count():
                self.create(name=n)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    references_num = models.PositiveIntegerField(default=0)

    objects = TagManager()

    def __str__(self):
        return '{} {}'.format(self.name, self.references_num)

class LikeDislike(models.Model):
    like_dislike = models.AutoField(primary_key=True)

    LIKE = 1
    DISLIKE = -1
    VOTES = ((LIKE, 'Like'), (DISLIKE, 'Dislike'))

    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    vote = models.SmallIntegerField(choices=VOTES)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return '{} {}'.format(self.user, self.vote)

class QuestionManager(models.Manager):
    def newest(self):
        return self.filter(is_active=True).order_by('-pub_date')
    
    def hottest(self):
        return self.filter(is_active=True).order_by('-rating')

    def by_tag(self, tag_name):
        return self.filter(is_active=True, tags__name=tag_name)

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(default=0, db_index=True)
    is_active = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=timezone.now, db_index=True)
    answers_number = models.PositiveIntegerField(default=0)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    
    # votes = GenericRelation(to=LikeDislike, related_query_name="question")
    likes = models.ManyToManyField(Profile, blank=True, related_name='question_likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='question_dislikes')

    objects = QuestionManager()

    def __str__(self):
        return '{} {}'.format(self.title, self.rating)
    
    def add_tags(self, tags):
        for tag in tags:
            self.tags.add(Tag.objects.filter(name=tag)[0])

class AnswerManager(models.Manager):
    def newest(self, id):
        q = Question.objects.get(pk=id)
        return self.filter(is_active=True, question=q).order_by('-pub_date')
    
    def hottest(self, id):
        q = Question.objects.get(pk=id)
        return self.filter(is_active=True, question=q).order_by('-rating')

class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    pub_date = models.DateTimeField(default=timezone.now)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    
    # votes = GenericRelation(to=LikeDislike, related_query_name="answer")
    likes = models.ManyToManyField(Profile, blank=True, related_name='answer_likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='answer_dislikes')

    objects = AnswerManager()

    def __str__(self):
        return '{} {}'.format(self.rating, self.text)


