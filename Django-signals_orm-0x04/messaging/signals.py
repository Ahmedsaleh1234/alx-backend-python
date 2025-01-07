from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from models import Notification, Message, MessageHistory
from django.contrib.auth.models import User


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

@receiver(post_save, sender=User)
def delete_related_data(sender, instance, **kwargs):
    Message.objects.filter(sender=instance).delete()
    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(edited_by=instance).delete()
