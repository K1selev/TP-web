from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from app.models import *
from faker import Faker
import random

USERS_COUNT = 10000
QUESTIONS_COUNT = 100000
ANSWERS_COUNT = 1000000
TAGS_COUNT = 10000

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_users()
        self.create_profiles()
        self.create_questions()
        self.create_answers()

    def create_users(self):
        users = []
        faker = Faker()
        for i in range(USERS_COUNT):
            users.append(User(username=faker.user_name() + str(i), password=make_password('password'), email=faker.email()))
        User.objects.bulk_create(users, USERS_COUNT)

    def create_profiles(self):
        profiles = []
        faker = Faker()
        users = User.objects.all()
        for i in range(USERS_COUNT):
            profiles.append(Profile(user=users[i], nickname=faker.word()))
        Profile.objects.bulk_create(profiles, USERS_COUNT)

    def create_questions(self):
        questions = []
        faker = Faker()
        users = Profile.objects.all()
        for i in range(QUESTIONS_COUNT):
            questions.append(Question(title=faker.sentence(), text=faker.text(), date_published=faker.date_time_this_year(), is_published=True, author=random.choice(users)))
        Question.objects.bulk_create(questions, QUESTIONS_COUNT)

    def create_answers(self):
        answers = []
        faker = Faker()
        questions = Question.objects.all()
        users = Profile.objects.all()
        for i in range(ANSWERS_COUNT):
            answers.append(Answer(text=faker.text(), correct=False, question=random.choice(questions), date_published=faker.date_time_this_year(), author=random.choice(users)))
        Answer.objects.bulk_create(answers, ANSWERS_COUNT)