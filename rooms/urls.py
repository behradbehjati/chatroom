from django.urls import path
from . import views
app_name='rooms'
urlpatterns=[
    path('home/',views.HomeView.as_view(),name='homeview'),
    path('<str:room_name>/',views.RoomView.as_view(),name='roomview'),
]