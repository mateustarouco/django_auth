from django.urls import path
from .functions import CreateNewUser, ChangePassword , DeleteUser 


urlpatterns = [
    path('newuser/', CreateNewUser),
    path('newpassword/', ChangePassword),
    path('deleteuser/', DeleteUser),
]
