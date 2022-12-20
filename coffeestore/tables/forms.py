from django import forms

from coffee.models import (
    Client, Manager, Coffee,
    TypeOfCoffee, Orders, Sale, Department
)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_id', 'address', 'phone', 'name', 'email', )


class ClientDelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_id', )


class CoffeeForm(forms.ModelForm):

    class Meta:
        model = Coffee
        fields = '__all__'


class CoffeeDelForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('coffee_code', )


class TypeForm(forms.ModelForm):

    class Meta:
        model = TypeOfCoffee
        fields = '__all__'


class TypeDelForm(forms.ModelForm):
    class Meta:
        model = TypeOfCoffee
        fields = ('coffee_code', )


class ManagerDelFrom(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ('manager_service_number', )


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'


class DepartmentDelFrom(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department_number', )


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class SaleDelFrom(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('invoice_number', )


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

class OrdersDelFrom(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('order_number', )


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
