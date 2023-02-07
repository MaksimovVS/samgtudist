# samgtudist
## Сайт примеров студенческих работ


### Для запуска проекта (для Windows):

Склонируйте и перейдите в папку с репозиторием:
```bash
git clone git@github.com:MaksimovVS/samgtudist.git
cd samgtudist
```
Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```
Установите зависимости:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполните миграции и запустите сервер:
```bash
python manage.py migrate
python manage.py runserver
```

#### Просмотр документации API

После запуска сервера, перейдите по адресу:
```bash
http://127.0.0.1:8000/swagger-ui/
```

#### Работа с API

Создайте суперпользователя
```bash
python manage.py createsuperuser
```

Введите username, email, password
```bash
Username: Admin
Email address: Admin@example.ru
Password: Admin
Password (again): Admin
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
```

Через приложение Postman (или аналог) отправьте POST запрос на адрес:

http://127.0.0.1:8000/api/v1/jwt/create/

```bash
{
    "username": "Admin",
    "password": "Admin"
}
```

Придет ответ в формате: 

```bash
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MzM5MDUyNCwianRpIjoiM2Y4MTk0YTNjNzIxNDMzY2ExMWQ2ODdlY2YxNDM3ZTMiLCJ1c2VyX2lkIjoyfQ.bKlokQvCExyjbenq2wpc_-UsFtTcCnwzCgG01avb53g",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczMzkwNTI0LCJqdGkiOiI4NzhiMzFjYTM5Y2Q0YmFkYTNlNDQwYzBhNWQwYzVlZiIsInVzZXJfaWQiOjJ9.zCRd7Z3Z2y6TPpgnleGtu_ZxWRvgfrGZufEtLVR454c"
}
```

Копируем "access" токен. Вставляем его в графе Authorizations в графе
"Bearer Token".

### Технологии
- Django==4.1.5
- djangorestframework==3.14.0
- Pillow==9.4.0
- python-dotenv==0.19.0
- PyJWT==2.6.0
- djoser==2.1.0
- djangorestframework-simplejwt==4.8.0

# Инструкция для деплоя

## Настройка проекта django
1. Склонируйте и перейдите в папку с репозиторием:
```bash
git clone git@github.com:MaksimovVS/samgtudist.git
cd samgtudist
```
2. Создайте и активируйте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Выполните миграции:
```bash
python manage.py migrate
```
5. В файле samgtudist/config-example.json укажите свои
данные и переименуйте в config.json

6. Создайте суперпользователя и укажите данные, которые запросит скрипт (эти данные в будущем понадобятся для админки джанго)
```bash
python3 manage.py createsuperuser
```
7. Запустите сервер следующей командой
```bash
python manage.py runserver 0.0.0.0:8000
```
8. Если на этом этапе в браузере появляется приложение, значит всё сделано правильно

## Настройка uWSGI

1. Установим необходимые зависимости
```bash
sudo apt-get install python3.8-dev
sudo apt-get install gcc
pip install uwsgi
```
2. Запустим uwsgi сервер следующей командой (находясь в корне django-проекта):
```bash
uwsgi --http :8000 --module samgtudist.wsgi
```
3. Если в браузере на порту :8000 появляется приложение, значит всё работает правильно

## Настройка nginx для работы с uwsgi

1. Устанавливаем nginx, если он не установлен
```bash
sudo apt-get install nginx
```
2. Создаём новый файл конфигурации в /etc/nginx/sites-available/samgtudist.conf и пишем в нём следующую конфигурацию (меняем айпи, путь до репозитория):

```
upstream django {
    server unix:///home/username/.../samgtudist/samgtudist/samgtudist.sock;
}

# configuration of the server
server {
    listen      80;
    server_name --айпи сервера;
    charset     utf-8;
    # max upload size
    client_max_body_size 75M;
    # Django media and static files
    location /media  {
        alias /home/username/.../samgtudist/samgtudist/media;
    }
    location /static {
        alias /home/username/.../samgtudist/samgtudist/static;
    }
    # Send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /home/username/.../samgtudist/samgtudist/uwsgi_params;
    }


}

```
3. Создаём файл /home/username/.../samgtudist/samgtudist/uwsgi_params и вставляем в него это:

```
uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;
uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;
uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;
```
4. Делаем симлинк в sites-available, чтобы nginx мог его увидеть

```bash
sudo ln -s /etc/nginx/sites-available/samgtudist.conf /etc/nginx/sites-enabled/
```

5. Находясь в корне django проекта, пишем следующую команду для наполнения папки static
```
python3 manage.py collectstatic
```
6. Перезагружаем nginx
```
sudo systemctl restart nginx
```
7. Проверяем, запускаем uwsgi следующей командой (находясь в корне Django проекта), и если в браузере появляется приложение, значит всё сделано правильно
```
uwsgi --socket samgtudist.sock --module samgtudist.wsgi --chmod-socket=666
```
8. В корне джанго проекта создаём файл samgtudist.ini со следующим содержанием
```
[uwsgi]
# Полный путь до корневой папки джанго проекта
chdir            = /home/username/.../samgtudist/samgtudist/
# Здесь ничего не меняем
module           = samgtudist.wsgi
# Полный путь до виртуального окружения
home             = /home/username/.../samgtudist/env/md
# enable uwsgi master process
master          = true
# maximum number of worker processes
processes       = 10
# Полный путь до сокета (находится в корне джанго проекта)
socket          = /home/username/.../samgtudist/samgtudist/samgtudist.sock
# socket permissions
chmod-socket    = 666
# clear environment on exit
vacuum          = true
# Путь до лог файла сервера
daemonize       = /home/username/logs/uwsgi-emperor.log                                                  
```
Теперь запустить приложение можно следующей командой:
```
uwsgi --ini home/username/.../samgtudist/samgtudist/microdomains_uwsgi.ini
```


