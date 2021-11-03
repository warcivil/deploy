from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from app.models import Todo
from app.application.services.serializers import TodoSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer