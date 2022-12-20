from django.contrib import admin
from django.urls import path, include
from .views import (
    ClientViewSet, ManagerViewSet, TypeOfCoffeeViewSet,
    CoffeeViewSet, OrdersViewSet, SaleViewSet, DepartmentViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('client', ClientViewSet)
router.register('manager', ManagerViewSet)
router.register('typeofcoffee', TypeOfCoffeeViewSet)
router.register('coffee', CoffeeViewSet)
router.register('orders', OrdersViewSet)
router.register('sale', SaleViewSet)
router.register('department', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
