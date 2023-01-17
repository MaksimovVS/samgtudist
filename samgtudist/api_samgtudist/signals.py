from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import File
from api_samgtudist.parser import parse_file


@receiver(post_save, sender = File)
def parse_material_document(sender, instance, created, **kwargs):
    "Сигнал, при сохранении документа парсит его на параграфы работы. Работает только при загрузке первого файла."
    if created:
        parse_file(instance)
        