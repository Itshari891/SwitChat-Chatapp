# SwitChat-Chatapp
This is a simple chat application built using the Python programming language and the Django web framework.
It allows users to communicate with each other in real-time through a web interface.
The application utilizes Django's built-in functionality for handling user authentication .
This project is not based on websocket.
The realtime chatting is possible using simple python logic.
=============================================================
In this project the Registration and login is through the admin page of django.this project only provides the interface of chat functionality.
Adding a friend for user is done manually though the django admin site.
=============================================================
==========       Models    =======================
- User
  User is created using the django admin site
  
- Profile
  The profile model have a OneToOne relationship with the user model.
  Created using the django admin site.
  The profile of user contains the profile picture ,name,friends .The friends field is related to the friends model via ManyToMany relationship.
  
- Friend
  The Friend model have a OneToOne relationship with the profile model.
  Created using the django admin site.
  
- Message
  The message model contains 4 fields :
  body,msg_sender,msg_receiver,seen.
  Body is the actual message.Msg_sender and msg_reciever are the user and the friend to whom he/she is sending the message respectively.
  Seen is a booleanfield which denotes whether the the message is seen by the user or not.
  
