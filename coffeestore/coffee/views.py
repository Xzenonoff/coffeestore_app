from .models import (
    Client, Manager, Coffee,
    TypeOfCoffee, Orders, Sale, Department
)
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    ClientSerializer, ManagerSerializer, CoffeeSerializer,
    TypeOfCoffeeSerializer, OrdersSerializer, SaleSerializer,
    DepartmentSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = '__all__'
    search_fields = ('name',)


class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = '__all__'
    search_fields = ('name',)


class CoffeeViewSet(ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = '__all__'
    search_fields = ('coffee_name',)


class TypeOfCoffeeViewSet(ModelViewSet):
    queryset = TypeOfCoffee.objects.all()
    serializer_class = TypeOfCoffeeSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = '__all__'
    search_fields = ('coffee_type_name',)


class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = '__all__'


class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = '__all__'


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = '__all__'
