from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Product, ProductImages, ProductReview, ProductSize, Wishlist, Tag

# Category Admin using DraggableMPTTAdmin to manage hierarchical data
@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name
    list_display = ('tree_actions', 'indented_title', 'related_products_count', 'related_products_cumulative_count')
    search_fields = ['name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs, Product, 'category', 'products_cumulative_count', cumulative=True
        )

        # Add non-cumulative product count
        qs = Category.objects.add_related_count(
            qs, Product, 'category', 'products_count', cumulative=False
        )

        return qs

    def related_products_count(self, instance):
        return instance.products_count

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_count.short_description = 'Direct products'
    related_products_cumulative_count.short_description = 'Total products (including children)'


# Inline admin to handle multiple images for a product
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1  # Allows adding more images directly from the product admin page


# Inline admin for ProductSize
class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


# Admin class for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price','discount', 'available', 'rating', 'created_at']
    list_filter = ['category', 'available', 'created_at']
    search_fields = ['category','name', 'description', 'category__name']
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name
    inlines = [ProductImagesInline, ProductSizeInline]  # Add inline forms for images and sizes
    readonly_fields = ['created_at', 'updated_at', 'rating', 'review_count']  # Rating and review count should be non-editable
    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'slug', 'description', 'price', 'discount', 'available', 'quantity', 'tags')
        }),
        ('Meta Data', {
            'fields': ('rating', 'review_count'),
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
        }),
    )


# Admin for ProductReview
@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'created_at']
    search_fields = ['user__username', 'product__name', 'rating']
    list_filter = ['rating', 'created_at']


# Admin for Wishlist
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__username']
    filter_horizontal = ['products']  # Provides a better UI for selecting multiple products


# Admin for Tags
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']

