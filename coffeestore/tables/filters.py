import django_filters
from coffee.models import (
    Client, Manager, Coffee,
    TypeOfCoffee, Orders, Sale, Department
)


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = '__all__'


class CoffeeFilter(django_filters.FilterSet):
    class Meta:
        model = Coffee
        fields = '__all__'


class ManagerFilter(django_filters.FilterSet):
    class Meta:
        model = Manager
        fields = '__all__'


class TypeOfCoffeeFilter(django_filters.FilterSet):
    class Meta:
        model = TypeOfCoffee
        fields = '__all__'


class OrdersFilter(django_filters.FilterSet):
    class Meta:
        model = Orders
        fields = '__all__'


class SaleFilter(django_filters.FilterSet):
    class Meta:
        model = Sale
        fields = '__all__'


class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = '__all__'
