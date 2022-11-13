
# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Client
from .serializers import ClientSerializer
from rest_framework import permissions


class ClientList(ListCreateAPIView):

    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)