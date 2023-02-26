from django.db import models
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import CharField, TextField

from hitcount.models import HitCountMixin, HitCount


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
                  ("rgr", "Расчетно-графическая работа"),
                  ("pz", "Пояснительная записка"),
                  ("upp", "Учебная/Производственная практика"),
                  ("vkr", "Выпускная квалификационная работа"),
                  ("test", "Тест"),
                  ("chert", "Чертеж"),
                  ("eskiz", "Эскиз"),
                  ("maket", "Макет"),
                  ("lkc", "Лекция"),
                  ("tr", "Типовой расчет"),
                  ("esse", "Эссе"),
                  ("exam", "Экзамен"),
                  ("ex_anw", "Ответы на вопросы для экамена"),
                  ("ans_test", "Ответы к тесту"),
                  ("dl", "Доклад"),
                  ("rt", "Рабочая Тетрадь"),
                  ("ref", "Реферат"),
                  ("pos", "Методические пособие"),
                  ("task", "Задача"),
                  ("var", "Другое"),
                  )


class Subject(models.Model):
    subject_title = models.CharField(
        "Название дисциплины",
        help_text="Введите название дисциплины",
        max_length=256,
    )

    def __str__(self) -> CharField:
        return self.subject_title

    class Meta:
        ordering = ('subject_title',)
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Material(models.Model, HitCountMixin):
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
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self) -> CharField:
        return self.material_title

    class Meta:
        ordering = ('material_title', '-created_date')
        verbose_name = "Работа"
        verbose_name_plural = "Работы"


class Paragraph(models.Model):
    paragraph_text = models.TextField(
        "Цитата",
        help_text="Введите цитату",
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="paragraph",
    )

    def __str__(self) -> TextField:
        return self.paragraph_text

    class Meta:
        verbose_name = "Абзац"
        verbose_name_plural = "Абзацы"


class Picture(models.Model):
    image = models.ImageField(
        "Иллюстрации к работе",
        # upload_to=file_save_path
        upload_to="image"
    )
    material = models.ForeignKey(
        "Material",
        on_delete=models.CASCADE,
        related_name="images"
    )


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

    def save(self, *args, **kwargs) -> None:
        file_type = self.file.name.split('.')[-1]
        self.file_type = file_type
        return super().save(self, *args, **kwargs)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


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
        ordering = ('last_name',)
        verbose_name = "Команда"
        # verbose_name_plural = "Команды"


class MaterialFileInline(admin.TabularInline):
    model = File


class ParagraphInline(admin.TabularInline):
    model = Paragraph


class PictureInline(admin.TabularInline):
    model = Picture


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    inlines = (MaterialFileInline, ParagraphInline, PictureInline)
