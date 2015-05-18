from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from datetime import *
from models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate


@login_required
def index(request):
    e = Employee.objects.get(user=request.user)
    return render(request, 'index.html', {'user': request.user, 'e': e})


@login_required
def products(request):
    allproducts = Product.objects.all()
    return render(request, 'products.html', {'products': allproducts, 'user': request.user})


@login_required
def product_details(request, pid):
    p = Product.objects.get(id=pid)
    s = Stock.objects.filter(product=pid)
    return render(request, 'product_details.html', {'p': p, 's': s, 'user': request.user})


@login_required
def invoices(request):
    i = Invoice.objects.all()
    return render(request, 'invoices.html', {'i': i, 'user': request.user})


@login_required
def invoice_details(request, iid):
    i = Invoice.objects.get(id=iid)
    p = Purchase.objects.filter(invoice=iid)
    return render(request, 'invoice_details.html', {'i': i, 'p': p, 'user': request.user})


@login_required
def new_invoice(request):
    if request.method == 'GET':
        c = Customer.objects.all()
        s = Store.objects.all()
        return render_to_response('new_invoice.html', {'c': c, 's': s, 'user': request.user}, context_instance=RequestContext(request))
    if request.method == 'POST':
        c = request.POST['customer']
        s = request.POST['store']
        new = Invoice.objects.create(store=Store.objects.get(id=s), customer=Customer.objects.get(id=c), totalPrice=0)
        new.save()
        return HttpResponseRedirect("/invoice_details/" + str(new.id))


@login_required
def delete_invoice(request, iid):
    i = Invoice.objects.get(id=iid)
    if not i.isFinalized:
        p = Purchase.objects.filter(invoice=iid)
        i.delete()
        p.delete()
    return HttpResponseRedirect("/invoices/")


@login_required
def finalize_invoice(request, iid):
    i = Invoice.objects.get(id=iid)
    if not i.isFinalized:
        i.isFinalized = True
        i.save()
        i.customer.storeCredit = i.customer.storeCredit + i.totalPrice * 0.01
        i.customer.save()
    return HttpResponseRedirect("/invoices/")


@login_required
def add_product(request, iid):
    if request.method == 'GET':
        i = Invoice.objects.get(id=iid)
        if not i.isFinalized:
            stock = Stock.objects.filter(store=i.store).exclude(quantity=0)
            return render(request, 'add_product.html', {'i': i, 'stock': stock, 'user': request.user})
        else:
            return HttpResponseRedirect("/invoices/")
    if request.method == 'POST':
        i = Invoice.objects.get(id=iid)
        if not i.isFinalized:
            pid = request.POST['product']
            if pid == "":
                return HttpResponseRedirect("/invoice_details/" + str(i.id))
            q = request.POST['quantity']
            q = float(q)
            p = Product.objects.get(id=pid)
            stock = Stock.objects.get(product=p, store=i.store)
            if stock.quantity >= q:
                stock.quantity = stock.quantity - q
                stock.save()
                pur = Purchase.objects.filter(invoice=i.id, product=pid)
                if len(pur) == 0:
                    new = Purchase.objects.create(invoice=i, product=p, quantity=q, price=q*p.currentPrice)
                    new.save()
                    i.totalPrice = i.totalPrice + new.price
                    i.save()
                else:
                    pur = Purchase.objects.get(invoice=i.id, product=pid)
                    pur.quantity = pur.quantity + q
                    pur.price = pur.quantity*pur.product.currentPrice
                    pur.save()
                    i.totalPrice = i.totalPrice + q * pur.product.currentPrice
                    i.save()
        return HttpResponseRedirect("/invoice_details/" + str(i.id))


@login_required
def remove_product(request, iid):
    if request.method == 'GET':
        i = Invoice.objects.get(id=iid)
        if not i.isFinalized:
            pur = Purchase.objects.filter(invoice=i)
            return render(request, 'remove_product.html', {'i': i, 'pur': pur, 'user': request.user})
        else:
            return HttpResponseRedirect("/invoices/")
    if request.method == 'POST':
        i = Invoice.objects.get(id=iid)
        if not i.isFinalized:
            pid = request.POST['product']
            if pid == "":
                return HttpResponseRedirect("/invoice_details/" + str(i.id))
            q = request.POST['quantity']
            q = float(q)
            p = Product.objects.get(id=pid)
            pur = Purchase.objects.get(product=p, invoice=i)
            if pur is None:
                return HttpResponseRedirect("/invoice_details/" + str(i.id))
            elif pur.quantity == q:
                i.totalPrice = i.totalPrice - pur.price
                pur.delete()
                i.save()
                stock = Stock.objects.get(store=i.store, product=p)
                stock.quantity = stock.quantity + q
                stock.save()
                return HttpResponseRedirect("/invoice_details/" + str(i.id))
            elif pur.quantity > q:
                pur.quantity = pur.quantity - q
                i.totalPrice = i.totalPrice - pur.price
                pur.price = pur.quantity * pur.product.currentPrice
                i.totalPrice = i.totalPrice + pur.price
                i.save()
                pur.save()
                stock = Stock.objects.get(store=i.store, product=p)
                stock.quantity = stock.quantity + q
                stock.save()
                return HttpResponseRedirect("/invoice_details/" + str(i.id))
            else:
                return HttpResponseRedirect("/invoice_details/" + str(i.id))


@login_required
def recieve_shipment(request):
    sup = Supplier.objects.all()
    return render(request, 'recieve_shipment.html', {'sup': sup, 'user': request.user})


@login_required
def recieve_shipment2(request):
    if request.method == 'GET':
        return HttpResponseRedirect("/recieve_shipment/")
    if request.method == 'POST':
        supid = request.POST['supplier']
        sup = Supplier.objects.get(id=supid)
        p = Product.objects.filter(supplier=sup)
        stores = Store.objects.all()
        return render(request, 'recieve_shipment2.html', {'sup': sup, 'p': p, 's' : stores, 'user': request.user})


@login_required
def recieve_shipment3(request):
    if request.method == 'GET':
        return HttpResponseRedirect("/recieve_shipment/")
    if request.method == 'POST':
        supid = request.POST['supplier']
        sid = request.POST['store']
        pid = request.POST['product']
        q = float(request.POST['quantity'])
        sup = Supplier.objects.get(id=supid)
        s = Store.objects.get(id=sid)
        p = Product.objects.get(id=pid)
        new = Shipment.objects.create(product=p, supplier=sup, store=s, quantity=q, date=datetime.today())
        new.save()
        stock = Stock.objects.filter(store=s, product=p)
        if len(stock) == 0:
            stock = Stock.objects.create(product=p, store=s, quantity=q)
            stock.save()
        else:
            stock = Stock.objects.get(store=s, product=p)
            stock.quantity = stock.quantity + q
            stock.save()
        return HttpResponseRedirect("/product_details/" + str(p.id))


@login_required
def new_customer(request):
    if request.method == 'GET':
        return render_to_response('new_customer.html', context_instance=RequestContext(request))
    if request.method == 'POST':
        ssno = request.POST['ssno']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        phoneNumber = request.POST['phoneNumber']
        c = Customer.objects.filter(ssno=ssno)
        if len(c) == 0:
            c = Customer.objects.create(ssno=ssno, first_name=first_name, last_name=last_name, email=email, address=address,
                                        phoneNumber=phoneNumber, storeCredit=0)
            c.save()
        return HttpResponseRedirect("/")


@login_required
def new_product(request):
    if request.method == 'GET':
        m = Manufacturer.objects.all()
        s = Supplier.objects.all()
        sc = ServiceCenter.objects.all()
        return render_to_response('new_product.html', {'m': m, 's': s, 'sc': sc, 'user': request.user}, context_instance=RequestContext(request))
    if request.method == 'POST':
        mid = request.POST['manufacturer']
        name = request.POST['name']
        price = float(request.POST['price'])
        info = request.POST['info']
        category = request.POST['category']
        sid = request.POST['supplier']
        scid = request.POST['serviceCenter']
        m = Manufacturer.objects.get(id=mid)
        s = Supplier.objects.get(id=sid)
        sc = ServiceCenter.objects.get(id=scid)
        p = Product.objects.filter(manufacturer=m, name=name)
        if len(p) == 0:
            p = Product.objects.create(manufacturer=m, name=name, listingPrice=price, currentPrice=price, info=info,
                                       category=category, supplier=s, serviceCenter=sc)
            p.save()
        return HttpResponseRedirect("/browse_products/")


@login_required
def customers(request):
    allcustomers = Customer.objects.all()
    return render(request, 'customers.html', {'c': allcustomers, 'user': request.user})


@login_required
def customer_details(request, pid):
    c = Customer.objects.get(id=pid)
    oi = Invoice.objects.filter(customer=c, isFinalized=True)
    pi = Invoice.objects.filter(customer=c, isFinalized=False)
    return render(request, 'customer_details.html', {'c': c, 'pi': pi, 'oi': oi, 'user': request.user})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")


def login_view(request):
    if request.method == 'GET':
        return render_to_response('login.html', context_instance=RequestContext(request))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/login/")
        else:
            return HttpResponseRedirect("/login/")



