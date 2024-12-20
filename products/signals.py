import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ProductImage

# Сигнал для удаления изображения при удалении записи
@receiver(pre_delete, sender=ProductImage)
def delete_image(sender, instance, **kwargs):
    # Проверяем, что файл существует, и удаляем его
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
