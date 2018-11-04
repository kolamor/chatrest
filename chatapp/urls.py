from django.contrib import admin
from django.urls import path, include
from chatapp.views import *
 
urlpatterns = [
   
	path('room/', RoomApi.as_view()),
	path('dialog/', Dialog.as_view()),
	path('users/', AddUsersRoom.as_view()),
]