import json
from rest_framework.views import Response 
from rest_framework.decorators import api_view
from autentications.models import PersonalUser as User
from django.contrib.auth import authenticate, logout 


@api_view(['POST','GET']) 
def CreateNewUser(request):
    if request.method =='GET':
        return Response('')
    else:
        #get from response
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        faceId = request.data.get('faceId')
        bithday = request.data.get('bithday')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        #create new User
        u = User.objects.create_user(username, email, password)
        u.first_name = first_name
        u.last_name = last_name
        u.bithday = bithday
        u.faceId = faceId
        u.save()
        if u:
            return Response('user criado com sucesso')
        else:
            return Response('falha ao criar usuario')

@api_view(['POST','GET'])
def ChangePassword(request):
    if request.method == 'GET':
        return Response('')
    else:
        username = request.data.get('username')
        password = request.data.get('password')

        u = User.objects.get(username=username)
        print(u)
        u.set_password(password)
        u.save()

        if u:
            return Response('Senha alterada com sucesso')
        else:
            return Response('falha ao alterar senha')

@api_view(['POST','GET'])
def DeleteUser(request):
    if request.method == 'GET':
        return Response('')
    else:
        emploerNo = request.data.get('emploerNo')

        u = User.objects.get(emploerNo=emploerNo)
        u.delete()

        if u:
            return Response('usuario Deleteado sucesso')
        else:
            return Response('falha ao deletar usuario')


@api_view(['POST'])
def AuthUser(request , format=json):
    username = request.data.get('username')
    password = request.data.get('password')
    
    u = authenticate(username=username, password=password)
    
    queryset = User.objects.filter(username=username).values()
    str(queryset)
    if u:
        return Response(queryset)
    else:
        return Response('não autenticado')


@api_view(['POST'])
def  LogOut(request):
    emploerNo = request.data.get('emploerNo')
    u = User
    logout(u)

@api_view(['GET'])
def GetAuthUser(request):
    us = authenticate(username='mateus', password="Qwer56ui")
    current_user = us.is_authenticated
    print(current_user)
    u =True
    #u = u.is_authenticated
    if u:
        return Response('whatever')
    else:
        return Response('not')