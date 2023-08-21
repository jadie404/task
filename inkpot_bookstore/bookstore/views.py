from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book, Cart, CartItem
from django.contrib.auth.decorators import login_required

def register(request):
    """
    Register a new user.

    This function handles user registration using the UserCreationForm.

    :param request: The HTTP request object.
    :return: Redirect to the login page after successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'bookstore/register.html', {'form': form})

def home_page(request):
    """
    Display the home page.

    This function logs the user out and renders the home.html template.

    :param request: The HTTP request object.
    :return: Rendered home.html template.
    """
    logout(request)
    return render(request, 'bookstore/home.html')

def contact_us(request):
    if request.method == 'POST':
        # Handle the contact form submission here (you'll need to create a form for this).
        # After successful submission, redirect to a success page.
        return render(request, 'bookstore/contact_success.html')
    return render(request, 'bookstore/contact.html')

def about_us(request):
    return render(request, 'bookstore/about.html')

def checkout(request):
    return render(request, 'bookstore/checkout.html')
    
@login_required(login_url='login')
def add_to_cart(request, book_id):
    """
    Add a book to the shopping cart.

    This function adds a book to the user's shopping cart.

    :param request: The HTTP request object.
    :param book_id: The ID of the book to add to the cart.
    :return: Redirect to the home page after adding the book to the cart.
    """
    book = Book.objects.get(pk=book_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    # Create a new CartItem instance and associate it with the cart and book
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    
    # If the cart item already exists, increase its quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('home')


def login(request,user):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'bookstore/login.html', {'form': form})

def logout_view(request):
    return redirect('home')
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'bookstore/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'bookstore/register.html', {'form': form})
    
    

@login_required(login_url='login')
def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    # Create a new CartItem instance and associate it with the cart and book
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    
    # If the cart item already exists, increase its quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('home')

    
    
def remove_from_cart(request, cart_item_id):
    """
    Remove an item from the shopping cart.

    This function removes a cart item from the user's shopping cart.

    :param request: The HTTP request object.
    :param cart_item_id: The ID of the cart item to remove.
    :return: Redirect to the cart page after removing the item.
    """
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()

    return redirect('cart')  # Redirect to the cart page after removing an item

def cart_view(request):
    """
    Display the shopping cart.

    This function displays the contents of the user's shopping cart.

    :param request: The HTTP request object.
    :return: Rendered cart.html template with cart items and total price.
    """
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.book.price * item.quantity for item in cart_items)

    return render(request, 'bookstore/cart.html', {'cart_items': cart_items, 'total_price': total_price})
