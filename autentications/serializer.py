from rest_framework import serializers
from .models import PersonalUser


class PersonalUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalUser
        fields = ['id','username','faceId','bithday','faceId','last_login','first_name','last_name','date_joined','email','bithday']