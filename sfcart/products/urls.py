from django.urls import path
from .views import  product_main, product_detail,subcategories_htmx, category_wise_products, productlist_basedon_category
app_name = 'products'

urlpatterns = [
    path('product_main/', product_main, name='product_main_page'),
    path('product/<int:id>/',product_detail, name = 'product_detail'),
    path('category_wise_products/<int:category_id>/',category_wise_products, name = 'category_wise_products'),
    path('subcategories-htmx/<int:category_id>/',subcategories_htmx, name='subcategories_htmx'),
    path('productlist_basedon_category/<int:category_id>/',productlist_basedon_category, name='productlist_basedon_category'),

]