from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='send_message', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='recieve_message', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.sender} to {self.reciever}'

class Notifaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notifaction for {self.user}'



