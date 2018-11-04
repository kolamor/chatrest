from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from chatapp.models import Room, Chat
from chatapp.serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers)


# Create your views here.

class RoomApi(APIView):
	"""Комнаты чата"""
	def get(self, request):
		rooms = Room.objects.all()
		serializer = RoomSerializers(rooms, many=True)
		return Response({'data': serializer.data})

class Dialog(APIView):
	"""дивлог чата"""
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
			return Response({'status': 'Add'})
		else:
			return Response({'status': 'Error'})
