from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home_view, name='home'), 
    path('register/', register, name='register'),  
    path('login/', user_login, name='login'),  
    path('shop/', shop, name='shop'),  
    path('shop/category/<int:category_id>/', products_by_category, name='products_by_category'),
    path('shop_detail/<int:pk>/', shop_detail_view, name='shop_detail'),  
    path('logout/', user_logout, name='logout'),
]
