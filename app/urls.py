from rest_framework import routers
from django.urls import path, include
from . import views
from .views import Hello

# router = routers.DefaultRouter()
# router.register('hello', HelloWorld, 'hello')

# urlpatterns = [
#     # path('', include(router.urls)),
#     path('hello/', Hello.as_view(), name='hello')
# ]
