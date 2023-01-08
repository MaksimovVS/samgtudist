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
        "Название дисциплины",
        help_text="Введите название дисциплины",
        max_length=256,
    )

    class Meta:
        ordering = ['subject_title']


class Material(models.Model):
    material_title = models.CharField(
        "Название работы",
        help_text="Введите название работы",
        max_length=256,
    )
    created_date = models.DateTimeField(
        verbose_name="Дата добавления в БД",
        auto_now_add=True,
    )
    subject = models.ManyToManyField(
        Subject,
        related_name="materials_related",
        related_query_name="material"
        )


class Content(models.Model):
    content_text = models.TextField(
        "Содержание",
        help_text="Введите содержание работы",
    )
    material = models.OneToOneField(
        Material,
        on_delete=models.CASCADE,
    )


class Quote(models.Model):
    quote_text = models.TextField(
        "Цитата",
        help_text="Введите цитату",
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
    )


class File(models.Model):
    file_type = models.CharField(
        max_length=10,
        choices=FILES_TYPE,
    )
    file = models.FileField(
        # TODO file_save_path - функция,
        #  которая будет возращать путь для сохраниения файла формата ДИСЦИПЛИНА/РАБОТА
        upload_to=file_save_path,
        # TODO file_name - функция которая будет называть файл
        name=file_name
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
    )


class ExamplePage(models.Model):
    page = models.TextField(
        verbose_name="HTML текст",
        help_text="Сохраняется сгенерированный HTML текст для отображения на сайте",
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
    )


class Team(models.Model):
    first_name = models.CharField(
        "Имя",
        max_length=50,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=50,
    )
    git = models.URLField(
        "Ссылка на github",
        blank=True,
    )
    email = models.EmailField(
        "Ваш емэйл",
        blank=True,
    )
    photo = models.ImageField(
        "Фотография",
        upload_to="/team",
    )
    posn = models.CharField(
        "Роль в команде",
        max_length=128,
        choices=TEAM_JOB,
    )
