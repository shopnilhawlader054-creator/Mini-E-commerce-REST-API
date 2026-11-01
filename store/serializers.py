from rest_framework import serializers
from.models import Order,Product,Category


class CategorySerialize(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at']



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at']

class OrderSerializer(serializers.ModelSerializer):

     class Meta:
         model = Order
         fields = '__all__'
        #  read_only_fields = ['user','']
         

