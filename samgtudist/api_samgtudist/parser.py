import docx2txt
from os import listdir
from tempfile import TemporaryDirectory
from docx import Document
from api_samgtudist.models import File, Paragraph, Picture
from samgtudist.settings import MEDIA_ROOT


# TODO:
# 1 Удалить титульник

def parse_file(instance: File) -> None:
    if instance.file_type != 'docx':
        return

    file_path = instance.file.path

    # Выполнится если у работы не добавлены параграфы
    if not Paragraph.objects.filter(material=instance.material).all():
        Paragraph.objects.bulk_create(parse_paragraphs(file_path, instance))
        parse_images(file_path, instance)


def parse_paragraphs(file_path: str, instance: File) -> list[Paragraph]:
    doc = Document(file_path)
    paragraph_list = []

    # текущий параграф, который будет сохранен в бд
    current_par = ''

    for ph in doc.paragraphs:
        if len(current_par + ph.text) >= 500:
            paragraph_list.append(Paragraph(
                paragraph_text=current_par,
                material=instance.material))

            current_par = ''

        if ph.text:
            current_par += '\n' + ph.text

    return paragraph_list


def parse_images(file_path: str, instance: File) -> None:
    # разархивировать картинки в временную папку
    temp_dir = TemporaryDirectory(dir=MEDIA_ROOT + '/' + 'tmp/')

    docx2txt.process(file_path, temp_dir.name)

    # обрабатываем картинки в временной папке
    images = listdir(temp_dir.name)

    for img in images:
        img_name = instance.material.material_title + ' - ' + img
        image_temp_path = temp_dir.name + '/' + img

        with open(image_temp_path, 'rb') as file:
            image_instance = Picture(material=instance.material)
            image_instance.image.save(img_name, file, save=True)
