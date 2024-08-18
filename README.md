virtual environment setup

Menginstall virtual environment

(windows)
```
pip install virtualenv
```
(linux)
```
python3 -m pip install --user virtualenv
```
Membuat virtual environment
```
python -m venv myvenv
```
Menjalankan visrtual environment

(windows)
```
myvenv\Scripts\activate
```
(linux)
```
source myvenv/bin/activate
```
menginstall library yang diperlukan
```
pip install -r requirements.txt
```
django setup

menginstall django dan Pillow untuk upload gambar
```
pip install django Pillow
```
menginstall project django di direktori utama
```
django-admin startproject myproject .
```
menjalankan project django
```
python manage.py runserver
```
membuat aplikasi django
```
python manage.py startapp myapp
```
membuat user admin
```
python manage.py createsuperuser
```
membuat migration
```
python manage.py makemigrations <!--masukkan aplikasi django-->
```
migrate ke database
```
python manage.py migrate <!-- sesuaikan dengan konfigurasi database-->
```

module configuration

settings.py
```
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
```

```
<!-- static files -->

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

load static files(css, javascript, logo)

{% load static %}
href/src = "{% static 'css/style.css' %}"
```

```
block content

{% block content %}
    ...
{% endblock content %}
```

```
include/extends html page

{% include 'index.html' %}
{% extends 'index.html' %}
```

file yang perlu di konfigurasi
```
settings.py
admin.py
app/urls.py
project/urls.py
models.py
views.py
```

install packages
```
sudo apt update
sudo apt install python3-pip apache2 libapache2-mod-wsgi-py3 pythonpy
sudo apt install python3.12-venv
```

if use sqlite3 db
```
chmod 664 ~/myproject/db.sqlite3
```

```
sudo chown :www-data ~/myproject/db.sqlite3
sudo chown :www-data ~/myproject
sudo ufw delete allow 8000
sudo ufw allow 'Apache Full'
sudo apache2ctl configtest
```
