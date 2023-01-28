from django.shortcuts import render,redirect
from .models import Friend,Profile,Message
from .forms import MessageForm,LoginForm
from django.http import JsonResponse
import json
from django.views.generic import FormView
from django.contrib.auth import authenticate,login
# Create your views here.

class LoginView(FormView):
    template_name = "mychatapp/login.html"
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                user=request.user.profile
                friends=user.friends.all()
                context={"user":user,"friends":friends}
                return render(request,"mychatapp/index.html",context)
            else:
                return render(request, "mychatapp/login.html", {"form": form})




def index(request):
    user=request.user.profile
    friends=user.friends.all()
    context={"user":user,"friends":friends}
    return render(request,"mychatapp/index.html",context)


def detail(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    form=MessageForm()
    sender=request.user.profile
    receiver=Profile.objects.get(id=friend.profile.id)
    chats=Message.objects.all()
    rec_chats=Message.objects.filter(msg_sender=receiver,msg_receiver=sender)
    rec_chats.update(seen=True)
    if request.method=="POST":
        form=MessageForm(request.POST)
        if form.is_valid:
            chat_message=form.save(commit=False)
            chat_message.msg_sender=sender
            chat_message.msg_receiver=receiver
            chat_message.save()
            return redirect("detail",pk=friend.profile.id)
    context={"friend":friend,"form":form,"sender":sender,"receiver":receiver,"chats":chats,"num":rec_chats.count()}
    return render(request,"mychatapp/detail.html",context)

def sentMessages(request,pk):
    sender=request.user.profile
    receiver=Profile.objects.get(id=pk)
    data=json.loads(request.body)
    chat=data["msg"]
    chat_message=Message.objects.create(body=chat,msg_sender=sender,msg_receiver=receiver)
    print(chat)
    return JsonResponse(chat_message.body,safe=False)

def receiveMessages(request,pk):
    sender=request.user.profile
    receiver=Profile.objects.get(id=pk)
    rec_chat=[]
    chats=Message.objects.filter(msg_sender=receiver,msg_receiver=sender)
    for chat in chats:
        rec_chat.append(chat.body)
    return JsonResponse(rec_chat,safe=False)

def getNotification(request):
    sender=request.user.profile
    friends=sender.friends.all()
    rec_msg=[]
    for friend in friends:
        rec_chat=Message.objects.filter(msg_sender_id=friend.profile.id,msg_receiver=sender,seen=False)
        rec_msg.append(rec_chat.count())
    return JsonResponse(rec_msg,safe=False)