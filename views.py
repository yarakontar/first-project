from django.shortcuts import render
from .models import User
from .models import Products
from .models import Sale
from .serializers import (UserSerializer,ProductSerializer,SaleSerializer)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta
from django.db.models import Count
# from products import TranchMonth


# from datetime import date ,timedelta
# from django.db.models import Sum
# from django.db.models import Count
# from django.utils.timezone import now



# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetials(generics.RetrieveUpdateDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductsDetials(generics.RetrieveUpdateDestroyAPIView):
   queryset =Products.objects.all()
   serializer_class =ProductSerializer
   permission_classes = [IsAuthenticated]


class SalesList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]


class salesDetials(generics.RetrieveUpdateDestroyAPIView):
   queryset =Sale.objects.all()
   serializer_class =SaleSerializer
   permission_classes = [IsAuthenticated]



# def calculate_sales_average(queryset):
# # تاريخ اليوم
#     today = date.today()

# # تاريخ بداية الشهر الحالي
#     start_of_month = today.replace(day=1)

# # queryset لجميع المبيعات التي تمت للمنتج "product_name" خلال الفترة المحددة
#     sales_queryset = Products.objects.filter(product__name="product_name", date__range=[start_of_month, today])

# # مجموع المبيعات اليومية للمنتج "product_name"
#     daily_sales_count = Products.filter(date=today).count()

# # مجموع المبيعات الشهرية للمنتج "product_name"
#     monthly_sales_count = Products.annotate(month=TranchMonth('date')).values('month').annotate(count=Count('id')).values('count')[0]['count']

# # معدل المبيعات اليومية للمنتج "product_name"
#     average_daily_sales = daily_sales_count / today.day

# # معدل المبيعات الشهرية للمنتج "product_name"
#     average_monthly_sales = monthly_sales_count / today.month
#     return {'average_daily_sales': average_daily_sales, 'average_monthly_sales': average_monthly_sales}

