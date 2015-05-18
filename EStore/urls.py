from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'Main.views.index', name='index'),
    url(r'^products/', 'Main.views.products', name='products'),
    url(r'^product_details/(?P<pid>.*)', 'Main.views.product_details', name='product_details'),
    url(r'^invoices/', 'Main.views.invoices', name='invoices'),
    url(r'^invoice_details/(?P<iid>.*)', 'Main.views.invoice_details', name='invoice_details'),
    url(r'^new_invoice/', 'Main.views.new_invoice', name='new_invoice'),
    url(r'^delete_invoice/(?P<iid>.*)', 'Main.views.delete_invoice', name='delete_invoice'),
    url(r'^finalize_invoice/(?P<iid>.*)', 'Main.views.finalize_invoice', name='finalize_invoice'),
    url(r'^add_product/(?P<iid>.*)', 'Main.views.add_product', name='add_product'),
    url(r'^remove_product/(?P<iid>.*)', 'Main.views.remove_product', name='remove_product'),
    url(r'^recieve_shipment/', 'Main.views.recieve_shipment', name='recieve_shipment'),
    url(r'^recieve_shipment2/', 'Main.views.recieve_shipment2', name='recieve_shipment2'),
    url(r'^recieve_shipment3/', 'Main.views.recieve_shipment3', name='recieve_shipment3'),
    url(r'^new_customer/', 'Main.views.new_customer', name='new_customer'),
    url(r'^new_product/', 'Main.views.new_product', name='new_product'),
    url(r'^customers/', 'Main.views.customers', name='customers'),
    url(r'^customer_details/(?P<pid>.*)', 'Main.views.customer_details', name='customer_details'),
    url(r'^login/', 'Main.views.login_view', name='login_view'),
    url(r'^logout/', 'Main.views.logout_view', name='logout_view'),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
