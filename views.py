from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sympy import Product
from rest_framework import routers, serializers, viewsets

# Create your views here.
from .models import *
from .serializers import eshopserializer
from django.contrib.auth.hashers import check_password, make_password


def index(request):

    if request.method == "POST":
        product_id = request.POST.get('cart_id')
        cart_id = request.session.get('cart')
        remove = request.POST.get('minus')
        # print("--------",cart_id)

        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id] = 1

        else:
            cart_id = {}
            cart_id[product_id] = 1
        request.session['cart'] = cart_id
        # print("----------request.session['cart']---", request.session['cart'])

    cate = category.objects.all()

    cate_id = request.GET.get('category_id')
    if cate_id:
        pro = product.objects.filter(category=cate_id)

    else:
        pro = product.objects.all()

    context = {
        'category': cate,
        'pro': pro
    }
    return render(request, 'home.html', context=context)


def Signup(request):
    if request.method == "POST":
        frist_name = request.POST.get('fname')
        lats_name = request.POST.get('lname')
        email_id = request.POST.get('email')
        pass_word = request.POST.get('pwd')
        mob_ile = request.POST.get('mbl')
        gen_der = request.POST.get('gender')

        save_info = signup(firstname=frist_name, lastname=lats_name, email=email_id, password=make_password(pass_word),
                           gender=gen_der, mobile=mob_ile)
        save_info.save()

        return redirect('home')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            fetchObj = signup.objects.get(email=email)
            if check_password(password, fetchObj.password):
                request.session['name'] = fetchObj.firstname
                request.session['email'] = fetchObj.email
                request.session['customer_id'] = fetchObj.id
                return redirect('home')
            else:
                return HttpResponse("wrong password")
        except:
            return HttpResponse("wrong Email")


def logout(request):
    request.session.clear()
    return redirect('home')


def cart_info(request):
    cart_id = request.session.get('cart').keys()
    # print("------------",cart_id)
    filtered_product = product.objects.filter(id__in=cart_id)
    return render(request, 'cart.html', {'filtered_product': filtered_product})


def chackout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer_id')
        # print(address, mobile, customer)
        if not customer_id:
            return HttpResponse("Please login")
        cart = request.session.get('cart')
        Product = product.objects.filter(id__in=list(cart.keys()))
        for pro in Product:
            price = pro.price
            order_info = order_dtls(
                address=address, mobile=mobile, customer=signup(id=customer_id), quantity=cart.get(str(pro.id)), product=pro, price=price)
        order_info.save()

    request.session['cart'] = {}

    return redirect('cart')


def ord_info(request):

    customerid = request.session.get('customer_id')
    fetch_order = order_dtls.objects.filter(customer=customerid)

    tp = 0
    for i in fetch_order:
        tp = tp+(i.price * i.quantity)
    return render(request, 'order.html', {'fetch_dtls': fetch_order, 'tp': tp})


def contact(request):
    return render(request, 'contact.html')


class serializerview(viewsets.ModelViewSet):
    queryset = signup.objects.all()
    serializer_class = eshopserializer
