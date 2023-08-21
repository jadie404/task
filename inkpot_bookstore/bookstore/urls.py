from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views  # Import views from auth app
from bookstore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
     path('login/', auth_views.LoginView.as_view(template_name='bookstore/login.html'), name='login'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Update the logout URL
    path('', views.home_page, name='home'),
    path('contact/', views.contact_us, name='contact'),
    path('about/', views.about_us, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
