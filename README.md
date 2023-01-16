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
