from django.urls import path
from .views import (UserList,UserDetials,ProductsList,ProductsDetials,SalesList,salesDetials)
                    
urlpatterns = [ 
      path('list/', UserList.as_view(), name='user-list'),
      path('detial/<int:pk>', UserDetials.as_view(), name='user-details'),
      path('product/',ProductsList.as_view(), name='product-list'),
      path('product/<int:pk>',ProductsDetials.as_view(), name='product-detials'),
      path('sales/',SalesList.as_view(), name='sales-list'),
      path('sales/<int:pk>',salesDetials.as_view(), name='sales-detials'),
    #    path('avg/',calculate_sales_average,name='avg'),
      ]
