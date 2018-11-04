from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from chatapp.models import Room, Chat
from chatapp.serializers import (RoomSerializers, ChatSerializers,
								 ChatPostSerializers, UserSerializers)
from django.contrib.auth.models import User


# Create your views here.

class RoomApi(APIView):
	"""Комнаты чата"""
	def get(self, request):
		rooms = Room.objects.all()
		serializer = RoomSerializers(rooms, many=True)
		return Response({'data': serializer.data})

class Dialog(APIView):
	"""диалог чата"""
	permission_classes = [permissions.IsAuthenticated, ]
	# permission_classes = [permissions.AllowAny, ]

	def get(self, request):
		room = request.GET.get('room')
		chat = Chat.objects.filter(room=room)
		serializer = ChatSerializers(chat, many=True)
		return Response({'data' : serializer.data})


	def post(self, request):
		#room = request.data.get('room')
		dialog = ChatPostSerializers(data=request.data)
		if dialog.is_valid():
			dialog.save(user=request.user)
			return Response(status=201)
		else:
			return Response(status=400)


class AddUsersRoom(APIView):
	"""добавление юзеров в комнату чата"""
	def get(self, request):
		user = User.objects.all()
		serializer = UserSerializers(user, many=True)
		return Response(serializer.data)

	def post(self, request):
		room = request.data.get("room")
		user = request.data.get("user")
		try:
			room = Room.objects.get(id=room)
			room.invited.add(user)
			room.save()
			return Response(status=201)
		except:
			return Response(status=400)
