from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from autentications.functions import CreateNewUser
from autentications.views import PersonealUserViewsets
from autentications.urls import urlpatterns as autentications

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
router.register('users', PersonealUserViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include(autentications)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

