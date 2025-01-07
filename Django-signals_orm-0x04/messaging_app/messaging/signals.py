from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from models import Notification, Message, MessageHistory


@receiver(post_save, sender=Message)
def send_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message(sender, instance, **kwargs):
    if instance.pk:
        old_message = Message.objects.get(pk=instance)
        if old_message.content != instance.content:
            MessageHistory.objects.create(content=instance.content, edited_by=instance.sender)
