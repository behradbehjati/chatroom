from django.shortcuts import render
from django.views import View
class HomeView(View):
    def get(self,request):
        return render(request,'home/home.html')
class RoomView(View):
    def get(self,request,room_name):
        return render(request,'room/room.html',{'room_name':room_name})