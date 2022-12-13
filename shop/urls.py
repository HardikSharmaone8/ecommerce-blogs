from django.urls import path
from .import views

urlpatterns=[
    path('item',views.show_shop,name='showShopItems'),
    path("productview/<int:myid>",views.product_view,name='productview'),
    path("search",views.search,name="search"),
    path("contacts",views.contacts,name="Contact page"),
    path("checkout",views.checkout,name="check out button"),
    path("tracker",views.tracker,name="Track Your Order")
]