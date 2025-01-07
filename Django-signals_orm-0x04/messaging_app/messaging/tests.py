from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessagingTestCase(TestCase):
    def setUp(self):
        self.sender = User.objects.create(username='sender')
        self.receiver = User.objects.create(username='receiver')

    def test_message_notification(self):
        message = Message.objects.create(sender=self.sender, receiver=self.receiver, content="Hello!")
        notification = Notification.objects.get(user=self.receiver, message=message)
        self.assertFalse(notification.is_read)
        self.assertEqual(notification.user, self.receiver)
