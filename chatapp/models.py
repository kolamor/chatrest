from django.db import models
from django.contrib.auth.models import User
# from djoser.urls.base import User

# Create your models here.

class Room(models.Model):
	"""модель комнаты чата"""

	creater = models.ForeignKey(User, verbose_name='Комната чата',
								on_delete=models.CASCADE)
	invited = models.ManyToManyField(User, verbose_name='Участники',
									related_name='invated_user')
	date = models.DateTimeField('Дата создания', auto_now_add=True)

	class Meta:
		verbose_name = 'Комната чата'
		verbose_name_plural = 'Комнаты чатов'


class Chat(models.Model):
	""" Модель чата"""
	room = models.ForeignKey(Room, verbose_name='Комната чата',
							on_delete=models.CASCADE)
	user = models.ForeignKey(User, verbose_name='Пользователь',
							on_delete=models.CASCADE)
	text = models.TextField('Сообщения', max_length=500)
	date = models.DateTimeField('Дата отправки', auto_now_add=True)

	class Meta:
		verbose_name = 'Сообщении чата'
		verbose_name_plural = 'Сообщения чатов'
