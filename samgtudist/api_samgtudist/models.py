from django.db import models
from django.contrib import admin
from django.forms import TextInput, Textarea


FILES_TYPE = (("docx", "Word"),
              ("doc", "Word old"),
              ("pdf", "PDF"),
              ("jpeg", "Pictures"),
              ("xls", "Excel"),
              )

TEAM_JOB = (("DS", 'Design'),
            ("FD", 'Frontend Developer'),
            ("BD", 'Backend Developer'),
            ("PM", 'Project Manager'),
            ("TT", 'Tester'),
            )

MATERIALS_TYPE = (("kr", 'Курсовая работа'),
                  ("dr", "Дипломная работа"),
                  ("pr", "Практическая работа"),
                  ("lr", "Лабораторная работа"),
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
                  ("exam", "Экзамен"),
                  ("ex_anw", "Ответы на вопросы для экамена"),
                  # "Ответы к тесту",
                  ("dl", "Доклад"),
                  # "Рабочая Тетрадь",
                  # "Реферат",
                  ("pos", "Методические пособие"),
                  ("task", "Задача"),
                  # "Другое",
                  )


class Subject(models.Model):
    subject_title = models.CharField(
        "Название дисциплины",
        help_text="Введите название дисциплины",
        max_length=256,
    )

    def __str__(self) -> str:
        return self.subject_title

    class Meta:
        ordering = ['subject_title']
        verbose_name = ("Предмет")
        verbose_name_plural = ("Предметы")


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
        "Тип работы",
        help_text="Выберите соответсующий тип работы",
        max_length=32,
        choices=MATERIALS_TYPE,
    )
    subject = models.ManyToManyField(
        Subject,
        related_name="materials_related",
        related_query_name="material"
        )

    def __str__(self) -> str:
        return self.material_title

    class Meta:
        verbose_name = ("Работа")
        verbose_name_plural = ("Работы")


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

    class Meta:
        verbose_name = ("Содержание")
        verbose_name_plural = ("Содержания")

    def __str__(self) -> str:
        return self.content_text


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

    def __str__(self) -> str:
        return self.quote_text

    class Meta:
        verbose_name = ("Цитата")
        verbose_name_plural = ("Цитаты")


class File(models.Model):
    file_type = models.CharField(
        max_length=10,
        choices=FILES_TYPE,
    )
    file = models.FileField(
        # TODO file_save_path - функция,
        # которая будет возращать путь для
        # сохраниения файла формата ДИСЦИПЛИНА/РАБОТА
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

    class Meta:
        verbose_name = ("Файл")
        verbose_name_plural = ("Файлы")


class ExamplePage(models.Model):
    page = models.TextField(
        "HTML текст",
        help_text="Сохраняется сгенерированный HTML текст для отображения на сайте",
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="example_page",
    )

    def __str__(self) -> str:
        return self.page

    class Meta:
        verbose_name = ("Пример Страницы")
        verbose_name_plural = ("Примеры Страниц")


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

    class Meta:
        ordering = ['last_name']
        verbose_name = ("Команда")
        verbose_name_plural = ("Команда")


class MaterialInline(admin.TabularInline):
    model = Quote


class MaterialFileInline(admin.TabularInline):
    model = File


class MaterialContentInline(admin.TabularInline):
    model = Content


class MaterialExamplePageInline(admin.TabularInline):
    model = ExamplePage


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    inlines = [MaterialInline,
               MaterialFileInline,
               MaterialContentInline,
               MaterialExamplePageInline,]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }
