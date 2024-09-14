from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.messages import warning, success
from django.contrib.auth import logout
from .forms import CommentForm

def home_view(request):
    products = Product.objects.all().order_by('-id')
    footer = ForFooter.objects.all()
    recent_products = Product.objects.all().order_by('-id')[:4]

    context = {
        'products': products,
        'footer': footer,
        'recent_products': recent_products,
    }
    return render(request, 'index.html', context)


def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id).order_by('-created_at') 
    category = get_object_or_404(Category, id=category_id)
    
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'products_by_category.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Account created successfully')
                return redirect('main:login')
        else:
            messages.error(request, 'Passwords do not match')
    context = {
        'user': user,
    }
    
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main:home')
            else:
                messages.error(request, 'Your account is not active. Please check your email for activation.')
        else:
            messages.error(request, 'Invalid login credentials')
    
    return render(request, 'login.html')


def shop(request):
    min_price = request.GET.get('min_price', 0)  # Default qiymat 0
    max_price = request.GET.get('max_price', 500)  # Default qiymat 500
    
    categories = Category.objects.all()

    # Filtr narx bo'yicha
    products = Product.objects.filter(price__gte=min_price, price__lte=max_price).order_by('-id')

    context = {
        'products': products,
        'categories': categories,
        'min_price': min_price,
        'max_price': max_price,
    }

    # Ajax so'rovini tekshirish uchun
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'partials/products_list.html', context)
    
    return render(request, 'shop.html', context)


def shop_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('main:shop_detail', pk=product.pk)
    else:
        form = CommentForm()

    context = {
        'product': product,
        'comments': comments,
        'form': form,
    }
    return render(request, 'shop_detail.html', context)

def user_logout(request):
    logout(request)
    return redirect('main:home')
