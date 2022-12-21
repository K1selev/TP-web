from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Tag, Question, Answer
from random import choice, sample
from faker import Faker

f = Faker()

default_avatars = [
    '/static/img/avatar_1.png'
]

class Command(BaseCommand):
    help = 'Fill database with faker data'

    def add_arguments(self, parser):
        parser.add_argument('--profile', '-p', type=int)
        parser.add_argument('--tag', '-t', type=int)
        parser.add_argument('--question', '-q', type=int)
        parser.add_argument('--answer', '-a', type=int)

    def fill_profiles(self, count):
        for _ in range(count):
            u = User.objects.create_user(f.name(), f.email(), f.password())
            u.save()
            
            Profile.objects.create(
                rating=f.random_int(min=-100, max=100),
                avatar=choice(default_avatars),
                user=u
            )
    
    def fill_tags(self, count):
        for _ in range(count):
            Tag.objects.create(
                name=f.word(),
                references_num=0
            )
    
    def fill_questions(self, count):
        profiles_id = list(Profile.objects.values_list('id', flat=True))
        tags_id = list(Tag.objects.values_list('id', flat=True))
        
        for _ in range(count):
            rtng = f.random_int(min=0, max=len(profiles_id) - 1)
            q = Question.objects.create(
                title='. '.join(f.sentences(f.random_int(min=2, max=3))),
                text='. '.join(f.sentences(f.random_int(min=20, max=40))),
                rating=rtng,
                pub_date=f.date_time(),
                answers_number=0,
                author=Profile.objects.get(pk=choice(profiles_id))
            )
            q.save()

            cur_tags_id = sample(tags_id, f.random_int(min=1, max=5))
            for tag_id in cur_tags_id:
                t = Tag.objects.get(pk=tag_id)
                t.references_num += 1
                t.save()
                q.tags.add(t)
            
            likes_num = rtng
            profiles_id_like = sample(profiles_id, likes_num)
            
            for profile_id in profiles_id_like:
                q.likes.add(Profile.objects.get(pk=profile_id))
    
    def fill_answers(self, count):
        profiles_id = list(Profile.objects.values_list('id', flat=True))
        qeustions_id = list(Question.objects.values_list('id', flat=True))

        for _ in range(count):
            rtng = f.random_int(min=0, max=len(profiles_id) - 1)
            q = Question.objects.get(pk=choice(qeustions_id))
            q.answers_number += 1
            q.save()

            a = Answer.objects.create(
                text='. '.join(f.sentences(f.random_int(min=20, max=40))),
                is_correct=choice([True, False]),
                rating=rtng,
                pub_date=f.date_time(),
                question=q,
                author=Profile.objects.get(pk=choice(profiles_id))
            )
            a.save()

            likes_num = rtng
            profiles_id_like = sample(profiles_id, likes_num)
            
            for profile_id in profiles_id_like:
                q.likes.add(Profile.objects.get(pk=profile_id))


    def handle(self, *args, **options):
        if (options['profile']):
            self.fill_profiles(options.get('profile', 0))
        if (options['tag']):
            self.fill_tags(options.get('tag', 0))
        if (options['question']):
            self.fill_questions(options.get('question', 0))
        if (options['answer']):
            self.fill_answers(options.get('answer', 0))
        # if options['ratio']:
        #     ratio = options.get('ratio', 0)
        #     self.fill_profiles(ratio)
        #     self.fill_tags(ratio)
        #     self.fill_questions(ratio * 10)
        #     self.fill_answers(ratio * 100)

