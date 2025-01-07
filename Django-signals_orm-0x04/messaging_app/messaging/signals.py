from django.db.models.signals import post_save
from django.dispatch import receiver
from models import Notifaction, Message


@receiver(post_save, sender=Message)
def send_message(sender, instance, created, **kwargs):
    if created:
        Notifaction.objects.create(user=instance.receiver, message=instance)