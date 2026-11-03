from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Category,Product,Order
from.serializers import CategorySerialize,ProductSerializer,OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CategoryApiView(viewsets.ModelViewSet):
      queryset = Category.objects.all()
      serializer_class = CategorySerialize

class ProductApiView(viewsets.ModelViewSet):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      filter_backends = [DjangoFilterBackend]
      filterset_fields = {
    'category': ['exact'],
    'name':['exact'],
    'price': ['exact', 'gte', 'lte'],
}




class OrderViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
         serializer = OrderSerializer(data=request.data)
         if serializer.is_valid():
              serializer.save()
    def get(self,request):
         order = Order.objects.filter(user=self.request.user)
         order_id =request.query_params.get('pk')

         if order_id:
              order =order.filter(pk=order_id)
         serializer = OrderSerializer(order,many=True) 
         return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self,request,pk):
         order = Order.objects.get(pk=pk)
         order.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self, request, pk):
        item = Order.objects.get(pk=pk)
        serializer = OrderSerializer(item, data=request.data, partial=True) # partial=True is key
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         

         
    
    
    permission_classes = [IsAuthenticated]

      