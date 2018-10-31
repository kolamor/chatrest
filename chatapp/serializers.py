from rest_framework import serializers

from chatapp.models import Room, Chat
from django.contrib.auth.models import User



class UserSerializers(serializers.ModelSerializer):
	"""Сериализация пользователя"""
	class Meta:
		model = User
		fields = ("id", 'username')

class RoomSerializers(serializers.ModelSerializer):
	""" Серилизация комнат чата"""
	creater = UserSerializers()
	invited = UserSerializers(many=True)
	class Meta:
		model = Room
		fields = ('creater', 'invited', 'date')


class ChatSerializers(serializers.ModelSerializer):
	"""Сериализация чата"""
	user = UserSerializers
	class Meta:
		model = Chat
		fields =('user', 'text', 'date')


class ChatPostSerializers(serializers.ModelSerializer):
	"""Сериализация post чата"""
	class Meta:
		model = Chat
		fields =('room','text')




