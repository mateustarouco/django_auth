from django.contrib import admin
from django.urls import path, include
from .functions import CreateNewUser, ChangePassword , DeleteUser , AuthUser, GetAuthUser, LogOut


urlpatterns = [
    path('newuser/', CreateNewUser),
    path('newpassword/', ChangePassword),
    path('deleteuser/', DeleteUser),
    path('authuser/', AuthUser),
    path('isauth/', GetAuthUser),
    path('logout/', LogOut),
]
