from django.urls import path
from .views import ClientList, ClientDetailView


urlpatterns = [
    path('', ClientList.as_view()),
    path('<int:id>', ClientDetailView.as_view()),
]