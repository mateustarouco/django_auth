from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from autentications.functions import CreateNewUser
from autentications.views import PersonealUserViewsets
from autentications.urls import urlpatterns as autentications

router = routers.DefaultRouter()
router.register('users', PersonealUserViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include(autentications)),
]
