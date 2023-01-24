from django.contrib import admin


from .models import *

class ProductImageInline(admin.TabularInline):
    model=AuctionImage
    max_num=3
    

@admin.register(Auction)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageInline, ]
admin.site.register(Bid)
admin.site.register(AuctionCategory)
# admin.site.register(Bid)

