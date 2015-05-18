from django.contrib import admin
from models import *


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'department', 'salary')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('ssno', 'first_name', 'last_name', 'email', 'storeCredit')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'info')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class ServiceCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'store',  'date', 'totalPrice')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'listingPrice', 'currentPrice')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'product', 'quantity')


class ReturnAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'product', 'quantity')


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'supplier', 'store', 'product', 'quantity')


class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'quantity')

admin.site.register(Store, StoreAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(ServiceCenter, ServiceCenterAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Return, ReturnAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Stock, StockAdmin)