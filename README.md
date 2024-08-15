#virtual environment setup

##Menginstall virtual environment
###(windows)
pip install virtualenv
###(linux)
python3 -m pip install --user virtualenv

##Membuat virtual environment
python -m venv myvenv

##Menjalankan visrtual environment
###(windows)
myvenv\Scripts\activate
###(linux)
source myvenv/bin/activate

##menginstall library yang diperlukan
pip install -r requirements.txt

#django setup

##menginstall django dan Pillow untuk upload gambar
pip install django Pillow

##menginstall project django di direktori utama
django-admin startproject myproject .

##menjalankan project django
python manage.py runserver

##membuat aplikasi django
python manage.py startapp myapp

##membuat user admin
python manage.py createsuperuser

##membuat migration
python manage.py makemigrations <!--masukkan aplikasi django-->

##migrate ke database
python manage.py migrate <!-- sesuaikan dengan konfigurasi database-->

#module configuration

##settings.py

import os
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'images')

<!-- fyi
    MEDIA_ROOT is the path on the filesystem to the directory containing your static media
    MEDIA_URL is the url that makes the static media accessible over http
-->

INSTALLED_APPS = [
    ...,
    <!-- 'coffee', -->
    'coffee.apps.CoffeeConfig',

]
<!-- mysql -->
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
<!-- sqlite3 -->
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

<!-- static files -->
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

###load static files(css, javascript, logo)
{% load static %}
href/src = "{% static 'css/style.css' %}"

###block content
{% block content %}
    ...
{% endblock content %}
