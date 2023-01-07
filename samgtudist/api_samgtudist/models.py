from django.db import models


FILES_TYPE = ("docs", "doc", "pdf", "jpeg", "xls")

TEAM_JOB = ('Design',
            'Frontend Developer',
            'Backend Developer',
            'Project Manager',
            'Tester',
            )

class Subject(models.Model):
    subject_title = models.CharField(
        verbose_name="Название дисциплины",
        help_text="Введите название дисциплины",
        max_length=256,
    )

class Material(models.Model):
    material_title = models.CharField(
        verbose_name="Название работы",
        help_text="Введите название работы",
        max_length=256,
    )
    subject = models.ManyToManyField(
        Subject,
        )

class Content(models.Model):
    content_text = models.TextField(
        verbose_name="Содержание",
        help_text="Введите сожержание работы",
    )
    material = models.OneToOneField(
        Material,
        on_delete=models.CASCADE,
    )

class Quote(models.Model):
    quote_text = models.TextField(
        verbose_name="Цитата",
        help_text="Введите цитату",
    )
    material = models.OneToOneField(
        Material,
        on_delete=models.CASCADE,
    )

class File(models.Model):
    file_type = models.CharField(
        max_length=10,
        choices=FILES_TYPE,
    )
    file = models.FileField(
        # TODO file_save_path - функция, которая будет возращать путь для сохраниения файла формата ДИСЦИПЛИНА/РАБОТА
        upload_to=file_save_path,
        # TODO file_name - функция которая будет называть файл
        name=file_name
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
    )

class ExamplePage(models.Model):
    page = models.ImageField(
        verbose_name="Превью работы, доступное к показу на сайте",
        # TODO img_previev_page_save_path - функция, которая будет возращать путь для сохраниения файла формата ДИСЦИПЛИНА/РАБОТА/ИЗОБРАЖЕНИЕ
        upload_to=img_previev_page_save_path,
        # TODO img_previev_page_name - функция которая будет называть файл
        name=img_previev_page_name
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
    )

class Team(models.Model):
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=50,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=50,
    )
    git = models.URLField(
        verbose_name="Ссылка на github",
        blank=True,
    )
    email = models.EmailField(
        verbose_name="Ваш емэйл",
        blank=True,
    )
    photo = models.ImageField(
        upload_to="/team",
        verbose_name="Фотография",
    )
    posn = models.CharField(
        max_length=128,
        choices=TEAM_JOB,
    )