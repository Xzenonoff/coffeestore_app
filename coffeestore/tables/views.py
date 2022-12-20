import django_tables2 as tables
from coffee.models import (
    Client, Manager, Coffee,
    TypeOfCoffee, Orders, Sale, Department
)
from django.shortcuts import render, redirect, get_object_or_404

from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from .filters import ClientFilter, CoffeeFilter, ManagerFilter, \
    TypeOfCoffeeFilter, DepartmentFilter, SaleFilter, OrdersFilter
from .forms import ClientForm, ClientDelForm, CoffeeForm, CoffeeDelForm, \
    TypeForm, TypeDelForm, ManagerDelFrom, ManagerForm, DepartmentDelFrom, \
    DepartmentForm, SaleForm, SaleDelFrom, OrdersForm, OrdersDelFrom
from .tables import ClientTable, CoffeeTable, ManagerTable, TypeOfCoffeeTable, \
    DepartmentTable, SaleTable, OrdersTable


def index(request):
    return render(request, 'index.html')


class ClientListView(SingleTableMixin, FilterView):
    model = Client
    table_class = ClientTable
    template_name = 'client/client_list.html'
    filterset_class = ClientFilter


class CoffeeListView(SingleTableMixin, FilterView):
    model = Coffee
    table_class = CoffeeTable
    template_name = 'coffee/coffee_list.html'
    filterset_class = CoffeeFilter


class ManagerListView(SingleTableMixin, FilterView):
    model = Manager
    table_class = ManagerTable
    template_name = 'manager/manager_list.html'
    filterset_class = ManagerFilter


class TypeListView(SingleTableMixin, FilterView):
    model = TypeOfCoffee
    table_class = TypeOfCoffeeTable
    template_name = 'typeofcoffee/type_list.html'
    filterset_class = TypeOfCoffeeFilter


class DepartmentListView(SingleTableMixin, FilterView):
    model = Department
    table_class = DepartmentTable
    template_name = 'department/department_list.html'
    filterset_class = DepartmentFilter


class SaleListView(SingleTableMixin, FilterView):
    model = Sale
    table_class = SaleTable
    template_name = 'sale/sale_list.html'
    filterset_class = SaleFilter


class OrdersListView(SingleTableMixin, FilterView):
    model = Orders
    table_class = OrdersTable
    template_name = 'orders/orders_list.html'
    filterset_class = OrdersFilter


def client_create(request):
    form = ClientForm(request.POST or None)
    if not form.is_valid() or request.method != "POST":
        context = {
            'form': form,
        }
        return render(request, 'client/client_create.html', context)
    client = form.save(commit=False)
    client.save()
    return redirect('tables:client')


def client_delete(request):
    form = ClientDelForm(request.POST or None)
    context = {
        'form': form,
    }
    if not form.is_valid() or request.method != "POST":
        if not form.data:
            return render(request, 'client/client_delete.html', context)
        client = get_object_or_404(Client, pk=form.data['client_id'])
        if client:
            client.delete()
            return redirect('tables:client')
    return render(request, 'client/client_delete.html', context)


def coffee_create(request):
    form = CoffeeForm(request.POST or None)
    if not form.is_valid() or request.method != "POST":
        context = {
            'form': form,
        }
        return render(request, 'coffee/coffee_create.html', context)
    client = form.save(commit=False)
    client.save()
    return redirect('tables:coffee')


def coffee_delete(request):
    form = CoffeeDelForm(request.POST or None)
    context = {
        'form': form,
    }
    if not form.is_valid() or request.method != "POST":
        if not form.data:
            return render(request, 'coffee/coffee_delete.html', context)
        coffee = get_object_or_404(Coffee, pk=form.data['coffee_code'])
        if coffee:
            coffee.delete()
            return redirect('tables:coffee')
    return render(request, 'coffee/coffee_delete.html', context)


def type_create(request):
    form = TypeForm(request.POST or None)
    if not form.is_valid() or request.method != "POST":
        context = {
            'form': form,
        }
        return render(request, 'typeofcoffee/type_create.html', context)
    cof_type = form.save(commit=False)
    cof_type.save()
    return redirect('tables:type')


def type_delete(request):
    form = TypeDelForm(request.POST or None)
    context = {
        'form': form,
    }
    if not form.is_valid() or request.method != "POST":
        if not form.data:
            return render(request, 'typeofcoffee/type_delete.html', context)
        cof_type = get_object_or_404(TypeOfCoffee, pk=form.data['coffee_code'])
        if cof_type:
            cof_type.delete()
            return redirect('tables:type')
    return render(request, 'typeofcoffee/type_delete.html', context)


def manager_create(request):
    form = ManagerForm(request.POST or None)
    if not form.is_valid() or request.method != "POST":
        context = {
            'form': form,
        }
        return render(request, 'manager/manager_create.html', context)
    cof_type = form.save(commit=False)
    cof_type.save()
    return redirect('tables:manager')


def manager_delete(request):
    form = ManagerDelFrom(request.POST or None)
    context = {
        'form': form,
    }
    if not form.is_valid() or request.method != "POST":
        if not form.data:
            return render(request, 'manager/manager_delete.html', context)
        cof_type = get_object_or_404(Manager, pk=form.data['manager_service_number'])
        if cof_type:
            cof_type.delete()
            return redirect('tables:manager')
    return render(request, 'tables:manager', context)


def department_create(request):
    form = DepartmentForm(request.POST or None)
    if not form.is_valid() or request.method != "POST":
        context = {
            'form': form,
        }
        return render(request, 'department/department_create.html', context)
    cof_type = form.save(commit=False)
    cof_type.save()
    return redirect('tables:department')


def department_delete(request):
    form = DepartmentDelFrom(request.POST or None)
    context = {
        'form': form,
    }
    if not form.is_valid() or request.method != "POST":
        if not form.data:
            return render(request, 'department/department_delete.html', context)
        cof_type = get_object_or_404(Department, pk=form.data['department_number'])
        if cof_type:
            print(cof_type)
            cof_type.delete()
            return redirect('tables:department')
    return render(request, 'tables:department', context)


def sale_create(request):
    form = SaleForm(request.POST or None)
    if not form.is_valid() or request.method != "POST":
        context = {
            'form': form,
        }
        return render(request, 'sale/sale_create.html', context)
    cof_type = form.save(commit=False)
    cof_type.save()
    return redirect('tables:sale')


def sale_delete(request):
    form = SaleDelFrom(request.POST or None)
    context = {
        'form': form,
    }
    if not form.is_valid() or request.method != "POST":
        if not form.data:
            return render(request, 'sale/sale_delete.html', context)
        cof_type = get_object_or_404(Sale, pk=form.data['invoice_number'])
        if cof_type:
            cof_type.delete()
            return redirect('tables:sale')
    return render(request, 'tables:sale', context)


def orders_create(request):
    form = OrdersForm(request.POST or None)
    if not form.is_valid() or request.method != "POST":
        context = {
            'form': form,
        }
        return render(request, 'orders/orders_create.html', context)
    cof_type = form.save(commit=False)
    cof_type.save()
    return redirect('tables:orders')


def orders_delete(request):
    form = OrdersDelFrom(request.POST or None)
    context = {
        'form': form,
    }
    if not form.is_valid() or request.method != "POST":
        if not form.data:
            return render(request, 'orders/orders_delete.html', context)
        cof_type = get_object_or_404(Orders, pk=form.data['order_number'])
        if cof_type:
            cof_type.delete()
            return redirect('tables:orders')
    return render(request, 'tables:orders', context)