from django.urls import path
from .views import ClientListView, CoffeeListView, TypeListView, \
    ManagerListView, DepartmentListView, SaleListView, OrdersListView
from . import views
app_name = 'tables'

urlpatterns = [
    path('', views.index),
    path('client/', ClientListView.as_view(), name='client'),
    path('client/create/', views.client_create, name='client_create'),
    path('client/delete/', views.client_delete, name='client_delete'),

    path('coffee/', CoffeeListView.as_view(), name='coffee'),
    path('coffee/create/', views.coffee_create, name='coffee_create'),
    path('coffee/delete/', views.coffee_delete, name='coffee_delete'),

    path('type/', TypeListView.as_view(), name='type'),
    path('type/create/', views.type_create, name='type_create'),
    path('type/delete/', views.type_delete, name='type_delete'),

    path('manager/', ManagerListView.as_view(), name='manager'),
    path('manager/create/', views.manager_create, name='manager_create'),
    path('manager/delete/', views.manager_delete, name='manager_delete'),

    path('department/', DepartmentListView.as_view(), name='department'),
    path('department/create/', views.department_create, name='department_create'),
    path('department/delete/', views.department_delete, name='department_delete'),

    path('sale/', SaleListView.as_view(), name='sale'),
    path('sale/create/', views.sale_create, name='sale_create'),
    path('sale/delete/', views.sale_delete, name='sale_delete'),

    path('orders/', OrdersListView.as_view(), name='orders'),
    path('orders/create/', views.orders_create, name='orders_create'),
    path('orders/delete/', views.orders_delete, name='orders_delete'),
]