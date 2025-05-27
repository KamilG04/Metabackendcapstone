from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-detail'),
    path('bookings/', views.BookingsView.as_view(), name='bookings'),
    path('bookings/<int:pk>/', views.SingleBookingView.as_view(), name='booking-detail'),
]
