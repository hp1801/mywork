from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartDetailView, CartItemView, PlaceOrderView, OrderViewSet, OrderUpdateView

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('cart/items/', CartItemView.as_view(), name='cart_item_create'),
    path('cart/items/<int:item_id>/', CartItemView.as_view(), name='cart_item_update_delete'),
    path('place-order/', PlaceOrderView.as_view(), name='place_order'),
    path('orders/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('', include(router.urls)),
]