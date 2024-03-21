# Пошаговая инструкция по созданию проекта на Django
### Установка и настройка Django
##### Виртуальное окружение
###### Создаём виртуальное окружение в Linux или MacOS
- mkdir project
- cd project
- python3 -m venv venv
###### Далее активируем виртуальное окружение, чтобы все дальнейшие действия выполнялись внутри него.
- venv/bin/activate # Linux/MacOS
- venv\Scripts\activate # Windows
- venv\Scripts\activate.ps1 # Windows PowerShell
##### Установка Django 
- pip install django
##### Создание проекта
- django-admin startproject myproject
##### Запуск сервера и проверка работоспособности
- python manage.py runserver
##### Создание приложения для сайта рецептов
- python manage.py startapp recipes_app
##### Добавление приложения в проект
- INSTALLED_APPS = [
- 'django.contrib.admin',
- 'django.contrib.auth',
 'django.contrib.contenttypes',
- 'django.contrib.sessions',
- 'django.contrib.messages',
- 'django.contrib.staticfiles',
- 'recipes_app',
- ]
##### Добавим модели 
- myproject/recipes_app/models.py
##### Добавим представления 
- myproject/recipes_app/views.py

##### Добавим шаблоны в директорию (templates)
- myproject/recipes_app/templates
- base.html
- home.html
- recipe.html
- registration.html
- login.html
- logout.html
- add_edit_recipe.html
##### Формы (forms.py)
- myproject/recipes_app/forms.py
##### Пропишем маршруты (urls.py)
- myproject/recipes_app/urls.py
##### Добавим пакет pillow 
- pip install Pillow 
##### Создадим миграций
- python manage.py makemigrations recipe_app
##### Применение изменения к базе данных
- python manage.py migrate
##### Добавим стили
-  static/recipes_app/ccs/style.css
- static/recipes_app/js/script.js

##### Настройка подключения к базе данных
- Откроем страницу Базы данных на сайте pythonanywhere. 
- Для бесплатного использования нам доступна БД MySQL. Придумаем пароль доступа к базе данных.
- Его стоит запомнить, чтобы чуть позже подключить Django к БД. 

#### Подготовка к развёртыванию проекта на сервере
- на пример на сервере от pythonanywhere.com
- регистрируемся 
- внесём изменения в файл setting.py проекта
- выключаем режим отладки 
- DEBUG = False
- добавим две константы для включения 
- дополнительных режимов безопасности 
- import os
- SECRET_KEY = os.getenv('SECRET_KEY')
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- добавим к нашему хосту
- ALLOWED_HOSTS = [
    'sprig.pythonanywhere.com',
]
- добавим директорию для статики на сервере
- STATIC_URL = '/static/'
- STATIC_ROOT = os.path.join(BASE_DIR, 'static')
- MEDIA_URL = 'media/'
- MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
- подготовим базу данных на сервере
- пропишем в настройках адрес хоста к базе данных ,имя пользователя, имя базы данных
- DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sprig$default',
        'USER': 'sprig',
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST': 'sprig.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },

    }
}
- в терминале mysql на сайте сервера пропишем команду
- ALTER DATABASE sprig$default CHARACTER SET utf8 COLLATE
utf8_general_ci;
- чтобы не было проблем с сохранением и выгрузкой данных не на английском языке
- Подготавливаем файл requirements.txt
- в терминале проекта введём команду
- pip freeze > requirements.txt
- Запишем в requirements.txt ещё пару строк в конец файла
- mysqlclient
- python-dotenv
- Сохраняем изменения 
- Создаём новый пустой репозиторий
- Соединяем локальный и удалённый репозиторий
- git remote add origin https://github.com/AleksVasilievich/PythonDjango2.git
- git branch -M main
- git push -u origin main
##### Переходим на сайт pythonanywhere, открываем консоль и клонируем репозиторий
- git clone https://github.com/myusername/myproject.git
##### Настройка проекта на сервере
- После завершения клонирования остаёмся в консоли, запускаем команду на создание виртуального окружения:
- mkvirtualenv --python=/usr/bin/python3.10 virtualenv
##### Активация виртуального окружения происходит автоматически после создания.
##### Другой вариант 
- which python3.10     # укажет путь до папки с python3.10
- /usr/local/bin/python3.10   # в моём случае
- /usr/local/bin/python3.10 -m venv env # создаём виртуальное окружение
- 
##### Не закрывая консоль устанавливаем необходимые пакеты:
- cd myproject
- pip install -r requirements.txt
##### Создаём веб-приложение


