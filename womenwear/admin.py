from audioop import reverse
from os import link
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from.models import (
    product_table,
    customer,
    Cart,
    orderPlaced,
    Enquiries,
    contact,
    wishlist,coupon,
    oderItem
)
# Register your models here.
@admin.register(customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =['id','user','name','address','locality','city','zipcode','state']

@admin.register(product_table)
class product_tableModelAdmin(admin.ModelAdmin):
    list_display =['name','id','main_cat','sub_cat','art_no','desc']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product_table','quantity']

@admin.register(orderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','ordered_date','user','Total_price','product_info','customer','customer_info','quantity','updated_at','status']

    def customer_info(self, obj):
        link=reverse("admin:womenwear_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)



    def product_info(self, obj):
        link=reverse("admin:womenwear_product_table_change", args=[obj.product_table.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product_table.art_no)




@admin.register(Enquiries)
class EnquiriesModelAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_no','whatsapp','country','time']


@admin.register(contact)
class contactModelAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_no','topic','orderid','time']

@admin.register(wishlist)
class wishlistModelAdmin(admin.ModelAdmin):
    list_display=['user','product_table','quantity'] 

@admin.register(coupon)
class couponModelAdmin(admin.ModelAdmin):
    list_display=['coupon','discount'] 

@admin.register(oderItem)
class oderItemModelAdmin(admin.ModelAdmin):
    list_display=['order','product','price','quantity'] 


# def ART_info(self, obj):
#         link=reverse("admin:womenwear_product_table_change", args=[obj.product_table.pk])
#         return format_html('<a href="{}">{}</a>',link,obj.product_table.art_no)



