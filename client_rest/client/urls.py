from django.urls import path
from .views import ClientList, ClientDetailView
from .models import Client
from .serializers import ClientSerializer


urlpatterns = [
    path('hi', ClientList.as_view()),
    path('<int:id>', ClientDetailView.as_view()),
]