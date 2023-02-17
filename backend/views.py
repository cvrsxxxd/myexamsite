from django.shortcuts import render, redirect
from register.forms import CreateUserForm


def index(request):
    return render(request, 'backend/index.html')


def cart(request):
    return render(request, 'backend/cart.html')


#
#
def blog(request):
    return render(request, 'backend/blog.html')


#
#
def contact(request):
    return render(request, 'backend/contact.html')


#
#
def product(request):
    return render(request, 'backend/product.html')


#
#
def regular(request):
    return render(request, 'backend/regular.html')


#
#
def shop(request):
    return render(request, 'backend/shop.html')


#
#
def singleblog(request):
    return render(request, 'backend/blog_single.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'register/register.html', context)
