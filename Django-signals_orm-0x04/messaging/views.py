from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def delete_user():
    user = User
    user.delete()

