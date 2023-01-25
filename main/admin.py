from django.contrib import admin

from .models import *

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(ProductImage)


from .models import *

admin.site.register(Product)

admin.site.register(Category)
