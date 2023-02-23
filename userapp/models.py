from django.contrib.auth.models import AbstractUser
from django.db import models


class Chat(models.Model):
    chat_id = models.CharField('Telegram Id чата с пользователем',
                               max_length=250, db_index=True, null=False,
                               blank=False)
    dialogue_state = models.CharField('Этап диалога пользователя с ботом',
                                      default='START',max_length=250)

    # user = models.OneToOneField(User, related_name='profile', unique=True)


class Order(models.Model):
    title = models.CharField(max_length=250, blank=True)
    discription = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    USERNAME_FIELD = ""


class Storage(models.Model):
    message_text = models.TextField(blank=True)
    add_time = models.DateField(auto_now_add=True)
