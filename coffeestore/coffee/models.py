from django.db import models


class Client(models.Model):
    client_id = models.IntegerField(db_column='Client_id', primary_key=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    orderedamount = models.IntegerField(db_column='OrderedAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class Coffee(models.Model):
    coffee_code = models.OneToOneField('TypeOfCoffee', models.DO_NOTHING, db_column='Coffee_code', primary_key=True)  # Field name made lowercase.
    coffee_name = models.TextField(db_column='Coffee_name')  # Field name made lowercase.
    date_of_manufacture = models.DateField(db_column='Date_of_manufacture')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coffee'


class Department(models.Model):
    department_number = models.IntegerField(db_column='Department_number', primary_key=True)  # Field name made lowercase.
    department_name = models.TextField(db_column='Department_name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class Manager(models.Model):
    manager_service_number = models.IntegerField(db_column='Manager_service_number', primary_key=True)  # Field name made lowercase.
    department_number = models.ForeignKey(Department, models.DO_NOTHING, db_column='Department_number')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20)  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manager'


class Orders(models.Model):
    order_number = models.IntegerField(db_column='Order_number', primary_key=True)  # Field name made lowercase.
    coffee_code = models.ForeignKey(Coffee, models.DO_NOTHING, db_column='Coffee_code')  # Field name made lowercase.
    client_number = models.ForeignKey(Client, models.DO_NOTHING, db_column='Client_number')  # Field name made lowercase.
    order_date = models.DateField(db_column='Order_date')  # Field name made lowercase.
    order_amount = models.IntegerField(db_column='Order_amount')  # Field name made lowercase.
    execution_date = models.DateField(db_column='Execution_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('order_number', 'coffee_code', 'client_number'),)


class Sale(models.Model):
    invoice_number = models.IntegerField(db_column='Invoice_number', primary_key=True)  # Field name made lowercase.
    coffee_code = models.ForeignKey(Coffee, models.DO_NOTHING, db_column='Coffee_code')  # Field name made lowercase.
    manager_service_number = models.ForeignKey(Manager, models.DO_NOTHING, db_column='Manager_service_number')  # Field name made lowercase.
    date_of_sale = models.DateField(db_column='Date_of_sale')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    sale_amount = models.IntegerField(db_column='Sale_amount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sale'
        unique_together = (('invoice_number', 'coffee_code', 'manager_service_number'),)


class TypeOfCoffee(models.Model):
    coffee_code = models.IntegerField(db_column='Coffee_code', primary_key=True)  # Field name made lowercase.
    coffee_type_name = models.TextField(db_column='Coffee_type_name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type_of_coffee'
