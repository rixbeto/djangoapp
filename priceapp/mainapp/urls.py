from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .views import (
    Home,
    ProductList,
    CreateProducts,
    GetProduct,
    SetProductUser,
    GetNotification,
    ChangePrice,
    WatchNotification,
)


#Services
urlpatterns = [
    path(
        "",
        Home.as_view(),
        name="Home",
    ),
    path(
        "products",
        ProductList.as_view(),
        name="products",
    ),
    path(
        "products/<str:name>/",
        GetProduct.as_view(),
        name="products_by_name",
    ),
    path(
        "set_products",
        csrf_exempt(SetProductUser.as_view()),
        name="set_products",
    ),
    path(
        "mynotifications",
        GetNotification.as_view(),
        name='mynotifications',
    ),
    path(
        "change_price",
        ChangePrice.as_view(),
        name="change_price",
    ),
    path(
        "watched/<int:n>",
        WatchNotification.as_view(),
        name="watched",
    ),
    path(
        "createproducts",
        CreateProducts.as_view(),
        name="createproducts",
    ),
]