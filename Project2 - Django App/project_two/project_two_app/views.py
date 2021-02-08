from django.shortcuts import render, redirect
from .models import AdminRegistration, Product
import bcrypt
from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def AdminLogin(request):
    return render(request, 'LoginPage.html')

def Login(request):
    errors = {}
    user = AdminRegistration.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/dashboard/orders')
        else :
            errors['password'] = 'password invalid'
    else:
        errors['email'] = 'email is invalid'
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/signin')

def AdminReg(request):
    return render(request, 'RegistrationPage.html')

def Register(request):
    errors = AdminRegistration.objects.registration_validator(request.POST)
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    else:
        new_user = AdminRegistration.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash,
            confirm_password = pw_hash,
        )
        request.session["user_id"] = new_user.id
        return redirect('/signin')

def DashOrder(request):
    context = {
        "TheProduct": Product.objects.get(id=2),
    }
    return render(request, 'OrderDashboard.html', context)

def ShowOrders(request):
    return render(request, 'ShowOrder.html')

def DashProduct(request):
    context = {
        "TheProduct": Product.objects.get(id=2),
    }
    return render(request, 'ProductsDashboard.html', context)

def EditItemPage(request, TheProduct):
    product = Product.objects.get(id=TheProduct)
    context = {
        "TheProduct": product,
    }
    return render(request, 'EditProductPage.html', context)

def EditItem(request, TheProduct):
    if request.method == "POST":
        errors = Product.objects.product_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'product/edit/{TheProduct}')
    else:
        TheProduct = Product.objects.get(id=TheProduct)
        TheProduct.name = request.POST['name']
        TheProduct.description = request.POST['description']
        TheProduct.category = request.POST['category']
        TheProduct.save()
        return redirect('/dashboard/products')

def AddItemPage(request):
    return render(request, 'NewProductPage.html')

def AddItem(request):
    if request.method == "POST":
        errors = AdminRegistration.objects.product_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/product/addnew')
    else:
        product = Product.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            category = request.POST['category'],
        )
        request.session['new_product_id'] = product.id
    return redirect('/dashboard/products')

def Items(request):
    return render(request, 'Shop.html')

def ShowItem(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "TheProduct": product,
    }
    return render(request, 'Item.html', context)

def Cart(request):
    return render(request, 'Cart.html')

def Kill(request, TheProduct):
    Delete_Product = Product.objects.get(id=TheProduct)
    Delete_Product.delete()
    return redirect('/dashboard/products')