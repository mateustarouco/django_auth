from rest_framework import  viewsets
from .serializer import PersonalUserSerializer
from .models import PersonalUser

class PersonealUserViewsets(viewsets.ModelViewSet):
    queryset = PersonalUser.objects.all()
    serializer_class = PersonalUserSerializer
