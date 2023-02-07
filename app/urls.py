from rest_framework import routers
from django.urls import path, include
from .views import HelloWorld, RegisterView, LoginView, LogoutView, GetCSRFToken, VaccineViewSet, PatientViewSet, CheckAuthenticatedView

router = routers.DefaultRouter()
router.register('vaccines', VaccineViewSet, 'vaccines'),
router.register('patients', PatientViewSet, 'patients')

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', HelloWorld.as_view(), name='hello'),
    path('register/', RegisterView.as_view(), name='register'),
    path('csrf_cookie/', GetCSRFToken.as_view(), name='csrf'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

# token = s3tphzYGWFnYa0XLqzdEP5y6wUgMM1fW
# username = user2
# password = password