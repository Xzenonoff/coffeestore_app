import django_tables2 as tables
from coffee.models import (
    Client, Manager, Coffee,
    TypeOfCoffee, Orders, Sale, Department
)


class ClientTable(tables.Table):
    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap.html"
        fields = ('client_id', 'address', 'phone', 'name', 'email', 'orderedamount',)


class CoffeeTable(tables.Table):
    class Meta:
        model = Coffee
        template_name = "django_tables2/bootstrap.html"
        fields = ('coffee_code', 'coffee_name', 'date_of_manufacture',)


class ManagerTable(tables.Table):
    class Meta:
        model = Manager
        template_name = "django_tables2/bootstrap.html"
        fields = ('manager_service_number', 'department_number', 'name', 'phone', 'email',)


class TypeOfCoffeeTable(tables.Table):
    class Meta:
        model = TypeOfCoffee
        template_name = "django_tables2/bootstrap.html"
        fields = ('coffee_code', 'coffee_type_name',)


class OrdersTable(tables.Table):
    class Meta:
        model = Orders
        template_name = "django_tables2/bootstrap.html"
        fields = ('order_number', 'coffee_code', 'client_number', 'order_date', 'order_amount', 'execution_date',)


class SaleTable(tables.Table):
    class Meta:
        model = Sale
        template_name = "django_tables2/bootstrap.html"
        fields = ('invoice_number', 'coffee_code', 'manager_service_number', 'date_of_sale', 'quantity', 'sale_amount',)


class DepartmentTable(tables.Table):
    class Meta:
        model = Department
        template_name = "django_tables2/bootstrap.html"
        fields = ('department_number', 'department_name', )

