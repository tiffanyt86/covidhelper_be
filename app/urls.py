from rest_framework import routers
from django.urls import path, include
from .views import HelloWorld, RegisterView, LoginView, LogoutView, GetCSRFToken, VaccineViewSet, MyPatientsList, PatientViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('vaccines', VaccineViewSet, 'vaccines'),
router.register('patients', PatientViewSet, 'patients')

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', HelloWorld.as_view(), name='hello'),
    path('register/', RegisterView.as_view(), name='register'),
    path('csrf_cookie/', GetCSRFToken.as_view(), name='csrf'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('my_patients/', MyPatientsList.as_view(), name='my_patients')
]

# token = s3tphzYGWFnYa0XLqzdEP5y6wUgMM1fW
# username = user2
# password = password