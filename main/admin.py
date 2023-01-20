from django.contrib import admin

from .models import *

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(ProductImage)


from .models import *

class ProductImageInline(admin.TabularInline):
    model=ProductImage
    max_num=3
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageInline, ]

admin.site.register(Category)