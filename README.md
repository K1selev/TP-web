# Askme
В качестве задания был выполнен проект «Вопросы и Ответы». Этот сервис позволяет пользователям Интернета задавать вопросы и получать на них ответы. Возможности комментирования и голосования формируют сообщество и позволяет пользователям активно помогать другим. В качестве образца реализации был использован Stack Overflow.

## Запуск проекта

```python
python3 --version     'проверяем стоит ли питон и какой версии'
python3 -m venv venv     'виртуальное окружение для питона (изоляция, не засорять)'
source venv/bin/activate     'активация виртуального окружения'
pip install Django     'установка джанго'
pip3 freeze > requirements.txt     'туда пишутся все зависимости нашего проекта(библиотека)'
django-admin startproject askme .     'создание джанго проекта (точка показывает место где (. там же где находимся))'
python3 manage.py startapp app     'создание приложения'
python3 manage.py runserver     'запуск вебсервера'
```
## Работа с БД

```python
python3 [manage.py](http://manage.py/) makemigrations ask    'создание миграции для нашего приложения'
python3 [manage.py](http://manage.py/) sqlmigrate ask 0001    'вывод в терминал sql кода конкретной миграции'
sqlite3 db.sqlite3     'заглянуть в базу данных использую клиент sqlite3'
.schema books_book     'показать схему отношений (таблицу)'
python3 [manage.py] migrate books     'применение миграции'
python [manage.py] dbshell     'еще один инструмент открытия базы данных'
python3 [manage.py] createsuperuser     'создание учетной записи администратора'

python3 [manage.py] shell     'залезем в базу'
from books import models
authors = models.Author.objects.all()      'заселектили'
author_1 = authors.filter(id=1)      'заселектили первого'
str(author_1)     'вывод'

author_3 = models.Author(name='Petia')     'добавление данных в базу'
author_3.save()
```

## Скриншоты готового проекта
![ScreenShot](https://github.com/K1selev/TP-web/blob/main/templates/screen/home.png)
![ScreenShot](https://github.com/K1selev/TP-web/blob/main/templates/screen/auth.png)
![ScreenShot](https://github.com/K1selev/TP-web/blob/main/templates/screen/new_question.png)
![ScreenShot](https://github.com/K1selev/TP-web/blob/main/templates/screen/question.png)
![ScreenShot](https://github.com/K1selev/TP-web/blob/main/templates/screen/admin.png)

## Репозиторий с описанием ТЗ:
https://github.com/ziontab/tp-tasks/

## Админские права:
login: sergey <br />
pass: 123
