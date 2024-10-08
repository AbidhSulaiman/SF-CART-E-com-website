from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import random
from django.db.models import Q 

# Create your views here.

def product_main(request):
    all_categories = Category.objects.filter(parent__isnull=True)
    
    # All products 
    initial_products = list(Product.objects.filter(available=True)[:50])
    random.shuffle(initial_products)
    all_products = initial_products[:12]

    # top fasions
    fasions_category = get_object_or_404(Category, name = 'Fashion')
    fasion_sub_category = fasions_category.get_descendants(include_self=True)
    fasions_category_products = Product.objects.filter( Q(category=fasions_category) | Q(category__in=fasion_sub_category)).filter(available=True)[:50]
    random.shuffle(initial_products)
    fasions_category_products_show = fasions_category_products[:6]
    

    context = {
        'all_categories': all_categories,  # Ensure you're passing this to the template
        'all_products':all_products,
        'fasions_category_products':fasions_category_products_show
    }
    return render(request, 'category/product_main.html', context)


# product detail 
def product_detail(request, id):

    product = get_object_or_404(Product,id= id, available = True)
    
    product_category = Category.objects.filter(name=product.category).first()
    

    initial_products = list(Product.objects.filter(category=product_category, available=True)[:20])

    random.shuffle(initial_products)
    similar_products = initial_products[:5]

     
    context = {
        'product':product,
        'similar_products':similar_products,
        "selcted_product_id" : id
    }

    return render(request, 'category/product_detail.html', context)

# for showing subcategories under main category 

def subcategories_htmx(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.children.all()  

    return render(request, 'category/subcategory_list.html', {
        'subcategories': subcategories,
        'category_id': category_id,
    })


# to show category wise product in the subcategories 
def category_wise_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.children.all() 

    if subcategories:
        all_products = Product.objects.filter(category__in= subcategories)
    else:
        all_products = Product.objects.filter(category= category)

    context = {
        'category':category,
        'subcategories': subcategories,
        'category_id': category_id,
        'all_products':all_products
    }
    print(all_products)
    return render(request, 'category/category_wise_products.html', context)


# for product list based on the subcategory selected 
def productlist_basedon_category(request, category_id =None):

    category = get_object_or_404(Category, id=category_id)
   
    products = Product.objects.filter(category=category)
    

    context = {
        'category':category,
        'products':products,
    }
    return render(request, 'category/productlist_basedon_category.html', context)
