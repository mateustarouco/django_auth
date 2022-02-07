from rest_framework import  viewsets
from rest_framework.permissions import  IsAuthenticated
from .serializer import PersonalUserSerializer
from .models import PersonalUser

class PersonealUserViewsets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = PersonalUser.objects.all()
    serializer_class = PersonalUserSerializer
