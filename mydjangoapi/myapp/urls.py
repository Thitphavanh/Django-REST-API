from django.urls import path
from .views import *


urlpatterns = [
    path('', Home),
    path('api/all-product', all_product),
    path('api/post-product', post_product),
    path('api/update-product/<int:TID>', update_product)
]