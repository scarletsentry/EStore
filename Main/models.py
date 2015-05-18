from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()
    title = models.CharField(max_length=50)
    accessLevel = models.IntegerField()
    worksAt = models.ForeignKey(Store)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Customer(models.Model):
    ssno = models.CharField(max_length=100, blank=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=255)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=50)
    storeCredit = models.FloatField()

    def __str__(self):
        return self.ssno


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=255, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    contactInfo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contactInfo = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceCenter(models.Model):
    name = models.CharField(max_length=100)
    contactInfo = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    listingPrice = models.FloatField()
    currentPrice = models.FloatField()
    info = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer)
    supplier = models.ForeignKey(Supplier)
    serviceCenter = models.ForeignKey(ServiceCenter)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    customer = models.ForeignKey(Customer)
    store = models.ForeignKey(Store)
    date = models.DateTimeField(auto_now=True)
    isFinalized = models.BooleanField(default=False)
    totalPrice = models.FloatField()

    def __str__(self):
        return str(self.id)


class Purchase(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    invoice = models.ForeignKey(Invoice)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)


class Return(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    invoice = models.ForeignKey(Invoice)
    reason = models.TextField()

    def __str__(self):
        return str(self.id)


class Shipment(models.Model):
    product = models.ForeignKey(Product)
    supplier = models.ForeignKey(Supplier)
    store = models.ForeignKey(Store)
    date = models.DateTimeField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Stock(models.Model):
    product = models.ForeignKey(Product)
    store = models.ForeignKey(Store)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)






