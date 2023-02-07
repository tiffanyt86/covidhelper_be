from rest_framework import routers
from django.urls import path
from .views import HelloWorld, RegisterView, LoginView, LogoutView, GetCSRFToken, CheckAuthenticatedView

# router = routers.DefaultRouter()
# router.register('hello/', HelloWorld, 'hello')

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello'),
    path('register/', RegisterView.as_view(), name='register'),
    path('csrf_cookie/', GetCSRFToken.as_view(), name='csrf'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
#     # path('', include(router.urls)),
#     path('hello/', Hello.as_view(), name='hello')
]

# path('hello/', HelloWorld.as_view(), name='hello'),
# path('register/', RegisterView.as_view(), name='register') 

# token = s3tphzYGWFnYa0XLqzdEP5y6wUgMM1fW
# username = user2
# password = password