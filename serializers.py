from rest_framework import serializers
from .models import User,Products,Sale




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

        
class UserSerializer(serializers.ModelSerializer):
     user = ProductSerializer(many=True,read_only = True),
       
     class Meta:
        model = User
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Sale
        fields = '__all__'
