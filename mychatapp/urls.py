from django.urls import path
from . import views

urlpatterns=[
    path("login",views.LoginView.as_view(),name="login"),
    path("",views.index,name="index"),
    path("friend/<str:pk>",views.detail,name="detail"),
    path("sent_msg/<str:pk>",views.sentMessages,name="sent_msg"),
    path("rec_msg/<str:pk>",views.receiveMessages,name="rec_msg"),
    path("notification",views.getNotification,name="notification"),

]