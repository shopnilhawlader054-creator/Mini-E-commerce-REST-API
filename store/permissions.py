from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets




class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    # এখানে পারমিশন ক্লাস যুক্ত করে দিতে হবে
    permission_classes = [IsAuthenticated]