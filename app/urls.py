from django.urls import path
from . import views
# from .views import generate_pwd

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_pwd, name='generated-password')
]