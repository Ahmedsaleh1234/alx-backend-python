from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Message
# Create your views here.

def delete_user(request):
    user = User
    user.delete()



def message_list(request):
    messages = Message.objects.filter(parent_message__isnull=True, sender=request.user).prefetch_related('replies').select_related('sender', 'receiver')
    
    return render(request, {'messages': messages})

def get_replies(message):
    replies = []
    for reply in message.replies.all().select_related('sender', 'receiver'):
        replies.append(reply)
        replies.extend(get_replies(reply))
    return replies

def threaded_message_view(request, message_id):
    message = Message.objects.select_related('sender', 'receiver').get(pk=message_id)
    replies = get_replies(message)
    
    return render(request,  {'message': message, 'replies': replies})



