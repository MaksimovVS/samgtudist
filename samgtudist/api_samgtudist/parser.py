from docx import Document
from .models import Material, File, Paragraph
from samgtudist.settings import MEDIA_ROOT


#TODO:
#1 Удалить титульник
#2 Парсинг Картинок

def parse_file(instance:File) -> None:

    if instance.file_type != 'docx':
        return

    file_path = instance.file.path

    #Выполнится если у работы не добавлены параграфы
    if not Paragraph.objects.filter(material = instance.material).all():
        Paragraph.objects.bulk_create(parse_paragraphs(file_path, instance))
    
    

def parse_paragraphs(file_path:str, instance:File) -> list[Paragraph]:
    doc = Document(file_path)
    paragraph_list = []
    
    #текущий параграф, который будет сохранен в бд
    current_par = ''
    
    for ph in doc.paragraphs:
        if len(current_par + ph.text) >= 500:
            paragraph_list.append(Paragraph(paragraph_text = current_par, material = instance.material))
            current_par = ''
            
        if ph.text:
            current_par += '\n' + ph.text

    return paragraph_list

def parse_images(document):
    pass