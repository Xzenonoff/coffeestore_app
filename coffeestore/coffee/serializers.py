from rest_framework import serializers
from .models import (
    Client, Manager, Coffee,
    TypeOfCoffee, Orders, Sale, Department
)


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Manager


class CoffeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Coffee


class TypeOfCoffeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = TypeOfCoffee


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Orders


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Sale


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Department
