from django.db import models


FILES_TYPE = (("docx", "Word"),
              ("doc", "Word old"),
              ("pdf", "PDF"),
              ("jpeg", "Pictures"),
              ("xls", "Excel"),
              )

TEAM_JOB = (("DS",'Design'),
            ("FD",'Frontend Developer'),
            ("BD",'Backend Developer'),
            ("PM",'Project Manager'),
            ("TT",'Tester'),
            )

MATERIALS_TYPE = (("kr",'Курсовая работа'),
                  ("dr","Дипломная работа"),
                  ("pr","Практическая работа"),
                  ("lr","Лабораторная работа"),
                  # "Расчетно-графическая работа",
                  # "Пояснительная записка",
                  # "Учебная/Производственная практика",
                  # "Выпускная квалификационная работа",
                  # "Тест",
                  # "Чертеж",
                  # "Эскиз",
                  # "Макет",
                  # "Лекция",
                  # "Типовой расчет",
                  # "Эссе",
                  # "Экзамен",
                  # "Ответы на вопросы",
                  # "Ответы к тесту",
                  # "Доклад",
                  # "Рабочая Тетрадь",
                  # "Реферат",
                  # "Методические указания",
                  # "Задача",
                  # "Другое",
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
    material_type = models.CharField(
        verbose_name="Тип работы",
        help_text="Выберите соответсующий тип работы",
        max_length=32,
        choices=MATERIALS_TYPE,
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
        related_name="content_text"
    )


class Quote(models.Model):
    quote_text = models.TextField(
        "Цитата",
        help_text="Введите цитату",
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="quotes",
        related_query_name="quotes_set"
    )


class File(models.Model):
    file_type = models.CharField(
        max_length=10,
        choices=FILES_TYPE,
    )
    file = models.FileField(
        # TODO file_save_path - функция,
        #  которая будет возращать путь для сохраниения файла формата ДИСЦИПЛИНА/РАБОТА
        # upload_to=file_save_path
        upload_to="works",
        # TODO file_name - функция которая будет называть файл
        # name=file_name
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="files_with_work"
    )


class ExamplePage(models.Model):
    page = models.TextField(
        verbose_name="HTML текст",
        help_text="Сохраняется сгенерированный HTML текст для отображения на сайте",
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="example_page",
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
        upload_to="team",
    )
    posn = models.CharField(
        "Роль в команде",
        max_length=128,
        choices=TEAM_JOB,
    )
