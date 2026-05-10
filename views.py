from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Dish
from .serializers import DishSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]