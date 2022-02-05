from django.db import models
from django.contrib.auth.models import AbstractUser


class PersonalUser(AbstractUser):
    emploerNo = models.BigAutoField( primary_key=True , unique=True )
    faceId = models.IntegerField(auto_created=True, blank=True, default=0)
    bithday = models.DateField(blank=True , null=True)

    def __str__(self):
        return str(self.emploerNo)
