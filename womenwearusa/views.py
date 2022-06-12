from ast import And
from audioop import add
from ctypes import Union
from http import client
from multiprocessing.dummy import JoinableQueue
from ntpath import join
from operator import index
from os import F_OK
from pickle import APPEND
from re import T
from django import dispatch
from django.contrib  import  messages
from django.core.mail import EmailMessage
from typing import Any
from unicodedata import name
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render ,redirect
from django.views import View
from razorpay import Customer
from womenwear.models import coupon, customer, orderPlaced, product_table ,Cart,Enquiries,contact,wishlist,coupon
from womenwear.forms import customerRegistraionForm , customer , CustomerProfileForm
from django.contrib import messages 
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
import razorpay
from django.template.loader import render_to_string
from django.core.paginator import Paginator

# Create your views here.

def womens_kurta(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1)
     data= request.POST.get('aa')
     data2= request.POST.get('ab')
     data3= request.POST.get('ac')
     data4= request.POST.get('ad')
     if data == "aa":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1).order_by('art_no')
          
     elif data2 == "ab":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1).order_by('sell_price')
          
     elif data3 == "ac":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1).order_by('-sell_price')
          
     elif data4 == "ad":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1).order_by('id')

     paginate=Paginator(dest1,10,orphans=5)
     page_number=request.GET.get('page')
     dest1final=paginate.get_page(page_number)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womens_kurta.html',{'dest1':dest1final,'totalitem':totalitem});

def WomenPalazzo_pants(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womenPalazzo&pants.html',{'totalitem':totalitem});

def WomenLehenga(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womenLehenga.html',{'totalitem':totalitem});

def WomenSkirts(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womenSkirts.html',{'totalitem':totalitem});

def WomenNight_Wear(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womenNightWear.html',{'totalitem':totalitem});

def WomenCasual_Wear(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womenCasual_Wear.html',{'totalitem':totalitem});

def WomenParty_Wear(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womenParty_Wear.html',{'totalitem':totalitem});

def WomenBlouse(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womenBlouse.html',{'totalitem':totalitem});

def HusbandShirts(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/husbandShirts.html',{'totalitem':totalitem});

def HusbandKurta(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/husbandKurta.html',{'totalitem':totalitem});

def HusbandEmbroideredkurta(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/husbandEmbroideredkurta.html',{'totalitem':totalitem});

def HusbandWaistcoat(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/husbandWaistcoat.html',{'totalitem':totalitem});

def HusbandShortkurta(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/husbandWaistcoat.html',{'totalitem':totalitem});

def HusbandKurtapajamaset(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/husbandKurtapajamaset.html',{'totalitem':totalitem});

def HusbandSherwani(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/husbandSherwani.html',{'totalitem':totalitem});

def HusbandNightWear(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/HusbandNightWear.html',{'totalitem':totalitem});

def KidsgirlsFrocks(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsgirlsFrocks.html',{'totalitem':totalitem});

def KidsgirlsKurtasets(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsgirlsFrocks.html',{'totalitem':totalitem});

def kidsgirlsTops_Tunics(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsgirlsTops_Tunics.html',{'totalitem':totalitem});

def kidsgirlsNight_Wear(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsgirlsNight_Wear.html',{'totalitem':totalitem});

def kidsgirlsLehengasets(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsgirlsLehengasets.html',{'totalitem':totalitem});

def kidsboysKurta(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsboysKurta.html',{'totalitem':totalitem});

def kidsboysKurtasets(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsboysKurtasets.html',{'totalitem':totalitem});

def kidsboysPartyWear(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsboysPartyWear.html',{'totalitem':totalitem});

def kidsboysShirt(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsboysShirt.html',{'totalitem':totalitem});

def kidsboysNightWear(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/kidsboysNightWear.html',{'totalitem':totalitem});

def Fashion_jewellery(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Fashion_jewellery.html',{'totalitem':totalitem});

def Earrings(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Earrings.html',{'totalitem':totalitem});     

def Flower_jewellery(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Flower_jewellery.html',{'totalitem':totalitem});     

def Silver_jewellery(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Silver_jewellery.html',{'totalitem':totalitem});     

def Necklace_Pendant(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Necklace_Pendant.html',{'totalitem':totalitem}); 

def Bracelets_Bangle(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Bracelets_Bangle.html',{'totalitem':totalitem}); 

def Ringsjewellery(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Rings.html',{'totalitem':totalitem});

def Hair_Accessories(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Hair_Accessories.html',{'totalitem':totalitem});

def Menjewellery(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Menjewellery.html',{'totalitem':totalitem});

def Kids_jewellery(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Kids_jewellery.html',{'totalitem':totalitem});

def Scarf(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Scarf.html',{'totalitem':totalitem});

def waistband(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/waistband.html',{'totalitem':totalitem});

def Potli(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Potli.html',{'totalitem':totalitem});

def Personal_care(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Personal_care.html',{'totalitem':totalitem});


def Wedding_Collection(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Wedding_Collection.html',{'totalitem':totalitem});

def Groom(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Groom.html',{'totalitem':totalitem});

def Bride(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Bride.html',{'totalitem':totalitem});

def Groom_Bride_Family(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Groom_Bride_Family.html',{'totalitem':totalitem});

def Bridesmaids(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Bridesmaids.html',{'totalitem':totalitem});

def Designer_Collection(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Designer_Collection.html',{'totalitem':totalitem});

def Under_799(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Under_799.html',{'totalitem':totalitem});

def Under_899(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Under_899.html',{'totalitem':totalitem});

def Under_999(request):
     totalitem = 0
     # wirte filter code for this page and render it 
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Under_999.html',{'totalitem':totalitem});


def women(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/women.html',{'dest1':dest1,'totalitem':totalitem});
def husband(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/husband.html',{'dest1':dest1,'totalitem':totalitem});
def accessories(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/accessories.html',{'dest1':dest1,'totalitem':totalitem});     

def Kids_Wear(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/Kids_Wear.html',{'dest1':dest1,'totalitem':totalitem});

def jewellery(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=1)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/jewellery.html',{'dest1':dest1,'totalitem':totalitem});

def womens_top(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=2).order_by('id')
     data= request.POST.get('aa')
     data2= request.POST.get('ab')
     data3= request.POST.get('ac')
     data4= request.POST.get('ad')
     if data == "aa":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=2).order_by('art_no')
          
     elif data2 == "ab":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=2).order_by('sell_price')
          
     elif data3 == "ac":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=2).order_by('-sell_price')
          
     elif data4 == "ad":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=2).order_by('id')
     paginate=Paginator(dest1,10,orphans=5)
     page_number=request.GET.get('page')
     dest1final=paginate.get_page(page_number)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womens_top.html',{'dest1':dest1final,'totalitem':totalitem});
def womens_goun(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=5).order_by('id')
     data= request.POST.get('aa')
     data2= request.POST.get('ab')
     data3= request.POST.get('ac')
     data4= request.POST.get('ad')
     if data == "aa":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=5).order_by('art_no')
          
     elif data2 == "ab":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=5).order_by('sell_price')
          
     elif data3 == "ac":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=5).order_by('-sell_price')
          
     elif data4 == "ad":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=5).order_by('id')
     paginate=Paginator(dest1,10,orphans=5)
     page_number=request.GET.get('page')
     dest1final=paginate.get_page(page_number)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womens_goun.html',{'dest1':dest1final,'totalitem':totalitem});
def womens_suit(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=3).order_by('id')
     data= request.POST.get('aa')
     data2= request.POST.get('ab')
     data3= request.POST.get('ac')
     data4= request.POST.get('ad')
     if data == "aa":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=3).order_by('art_no')
          
     elif data2 == "ab":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=3).order_by('sell_price')
          
     elif data3 == "ac":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=3).order_by('-sell_price')
          
     elif data4 == "ad":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=3).order_by('id')
     paginate=Paginator(dest1,10,orphans=5)
     page_number=request.GET.get('page')
     dest1final=paginate.get_page(page_number)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womens_suit.html',{'dest1':dest1final,'totalitem':totalitem});     
def womens_indo(request):
     totalitem = 0
     dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=4).order_by('id')
     data= request.POST.get('aa')
     data2= request.POST.get('ab')
     data3= request.POST.get('ac')
     data4= request.POST.get('ad')
     if data == "aa":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=4).order_by('art_no')
          
     elif data2 == "ab":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=4).order_by('sell_price')
          
     elif data3 == "ac":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=4).order_by('-sell_price')
          
     elif data4 == "ad":
          dest1 = product_table.objects.filter(main_cat=1,sub_cat=1,pro_cat=4).order_by('id')
     paginate=Paginator(dest1,10,orphans=5)
     page_number=request.GET.get('page')
     dest1final=paginate.get_page(page_number)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))    
     return render(request,'usa/womens_indo.html',{'dest1':dest1final,'totalitem':totalitem});
def home(request):   
     totalitem = 0
     dest1=product_table.objects.filter(main_cat=9,sub_cat=1,pro_cat=1,)
     dest2= product_table.objects.filter(main_cat=9,sub_cat=1,pro_cat=2)
     dest3= product_table.objects.filter(main_cat=9,sub_cat=1,pro_cat=3)
     dest4= product_table.objects.filter(main_cat=9,sub_cat=1,pro_cat=4)
         
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/index.html',{'totalitem':totalitem,'dest4':dest4,'dest1':dest1,'dest2':dest2,'dest3':dest3});



@login_required(login_url='signin/')
def checkout(request):
     totalitem = 0
     Coupon_message= None;
     code= None;
     amount = 0.0
     shipping_amount= 0
     totalamount = 0.0
     final=0
     form = CustomerProfileForm(request.POST)
     if form.is_valid():
          usr = request.user
          name = form.cleaned_data['name']
          address = form.cleaned_data['address']
          locality = form.cleaned_data['locality']
          city = form.cleaned_data['city']
          state = form.cleaned_data['state']
          zipcode = form.cleaned_data['zipcode']
          Mobile_no =form.cleaned_data['Mobile_no']
          Country =form.cleaned_data['country']
          reg = customer(user=usr,name=name,Mobile_no=Mobile_no,address=address,locality=locality,city=city,state=state,zipcode=zipcode,country=Country)
          reg.save()
          return redirect('checkout')
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     user = request.user
     add = customer.objects.filter(user = user)
     cart_items = Cart.objects.filter(user = user)
     Coupon= request.GET.get('coupon')
     if Coupon:
          try:
               code=coupon.objects.get(coupon=Coupon)
          except:
               Coupon_message='Invalid Coupon Code'
          cart_product = [p for p in Cart.objects.all() if p.user == request.user]
          if cart_product:
               for p in cart_product:
                    tempamount = (p.quantity * p.product_table.sell_price_usa)
                    amount += tempamount
                    totalamount = amount + shipping_amount  
                    discount = totalamount*0.2
                    final=totalamount - discount
                    pay_amount=final        
     else:
          cart_product = [p for p in Cart.objects.all() if p.user == request.user]
          if cart_product:
               for p in cart_product:
                    tempamount = (p.quantity * p.product_table.sell_price_usa)
                    amount += tempamount
                    totalamount = amount
                    pay_amount=int(totalamount) 
          client = razorpay.Client(auth =(settings.KEY,settings.SECRET))
          payment = client.order.create({'amount': pay_amount*100, "currency": "USD", "payment_capture": 1} )
     return render(request,'usa/checkout.html',{'form':form ,'totalamount':totalamount,'code':code,'Coupon_message':Coupon_message,'add':add,'final':final,'cart_items':cart_items,'totalitem':totalitem,'payment':payment});

def product(request,slug):
     totalitem = 0
     dest2 = product_table.objects.get(product_slug=slug)
     # dest3= price.objects.get(Product_table=dest2)
     # print(dest3)
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     item_already_in_cart = False
     if request.user.is_authenticated:       
       item_already_in_cart = Cart.objects.filter(Q(product_table = dest2.id) & Q(user=request.user)).exists()
     return render(request,'usa/product_details.html',{'dest2':dest2,'item_already_in_cart':item_already_in_cart,'totalitem':totalitem});

def about(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/about-us.html',{'totalitem':totalitem});

def Contact(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     if request.method =="POST":
          na=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          topic=request.POST.get('topic')
          orderid=request.POST.get('orderid')
          comment=request.POST.get('comment')
          data= contact(name=na,email=email,phone_no=phone,topic=topic,orderid=orderid,comment=comment)     
          data.save()
     else:
          pass
     messages.success(request,'Congratulation!! Profile Updated Successfully')
     return render(request,'usa/contact-us.html',{'totalitem':totalitem});

def policy(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/policy.html',{'totalitem':totalitem});

def exchange(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/exchange.html',{'totalitem':totalitem}); 

def payment(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/payment.html',{'totalitem':totalitem});

def shipping(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/shipping.html',{'totalitem':totalitem});   

def size(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/size.html',{'totalitem':totalitem});

def terms(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/terms.html',{'totalitem':totalitem});

def support(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/support.html',{'totalitem':totalitem}); 

def Wholesale(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     if request.method =="POST":
          na=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          Whatsapp=request.POST.get('Whatsapp')
          country=request.POST.get('country')
          comment=request.POST.get('comment')
          data= Enquiries(name=na,email=email,phone_no=phone,whatsapp=Whatsapp,country=country,enquiry=comment)     
          data.save()
     else:
          pass     
     return render(request,'usa/Wholesale.html',{'totalitem':totalitem});     

def international(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     return render(request,'usa/international.html',{'totalitem':totalitem});

@login_required
def order(request):
     totalitem=0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     op = orderPlaced.objects.filter(user=request.user)
     return render(request,'usa/order.html',{'order_placed':op,'totalitem':totalitem});


     
# def login(request):
#      return render(request,'login.html');
class CustomerRegistrationView(View):
     def get(self,request):
          form = customerRegistraionForm()
          return render(request,'../usa/templates/signup.html',{'form':form});
     def post(self,request):
          form = customerRegistraionForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,'congratulations your account has been created !!')
          return render(request,'../usa/templates/signup.html',{'form':form});

def search(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     searched = request.POST['searched']
     result= product_table.objects.filter(name__icontains= searched)
     return render(request,'usa/search_box.html',{'searched':searched,'result':result,'totalitem':totalitem});
 
# def profile(request):
#      return render(request,'profile.html'); 

@method_decorator(login_required ,name='dispatch')
class ProfileView(View):
     def get(self,request):
          totalitem = 0
          if request.user.is_authenticated:
              totalitem = len(Cart.objects.filter(user=request.user))
          form = CustomerProfileForm()
          return render(request,'usa/profile.html', {'form':form,'active':'btn-primary','totalitem':totalitem})
     def post(self,request):
          form = CustomerProfileForm(request.POST)
          totalitem = 0
          if request.user.is_authenticated:
              totalitem = len(Cart.objects.filter(user=request.user))
          if form.is_valid():
               usr = request.user
               name = form.cleaned_data['name']
               address = form.cleaned_data['address']
               locality = form.cleaned_data['locality']
               city = form.cleaned_data['city']
               state = form.cleaned_data['state']
               zipcode = form.cleaned_data['zipcode']
               Mobile_no =form.cleaned_data['Mobile_no']
               reg = customer(user=usr,name=name,Mobile_no=Mobile_no,address=address,locality=locality,city=city,state=state,zipcode=zipcode)
               reg.save()
               messages.success(request,'Congratulation!! Profile Updated Successfully')
          return render(request, 'usa/profile.html',{'form':form ,'active':'btn-primary','totalitem':totalitem})    
    
def address(request):
     add =customer.objects.filter(user=request.user)
     return render(request,'usa/address.html',{'add':add });

def list(request):
     user=request.user
     product_id=request.GET.get('prod_id')
     prod= product_table.objects.get(pk=product_id)
     wishlist(user=user,product_table=prod).save()
     cart = Cart.objects.filter(user=user)
     for c in cart:
          c.delete()
          return redirect('/usa/wishlist')

def remove_list(request):
     user=request.user
     product_id=request.GET.get('prod_id')
     wishlist(user=user,product_table=product_id)
     cart = wishlist.objects.filter(user=user)
     for c in cart:
          c.delete()
          return redirect('/usa/wishlist')

def Wishlist(request):
     totalitem = 0   
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user)) 
     wlist=wishlist.objects.filter(user=request.user).order_by('id') 
     dest2=wishlist.objects.all()       
     return render(request,'usa/wishlist.html',{'totalitem':totalitem,'wlist':wlist,'dest2':dest2});
     
@login_required(login_url='/signin/')
def cart(request):
     user=request.user
     product_id = request.GET.get('prod_id')
     product = product_table.objects.get(id=product_id)
     Cart(user=user , product_table=product).save()
     return redirect('/usa/cart')

@login_required(login_url='/signin/')
def removelist(request):
     user=request.user
     product_id = request.GET.get('prod_id')
     product = product_table.objects.get(id=product_id)
     Cart(user=user , product_table=product).save()
     cart = wishlist.objects.filter(user=user)
     for c in cart:
          c.delete()
     return redirect('/usa/cart')

def show_cart(request):   
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))          
     if request.user.is_authenticated:
         user = request.user
         cart = Cart.objects.filter(user=user)
     #     print(cart)
         amount = 0
         amount = 0
         dis=0
         Discount=0
         cart_product = [p for p in Cart.objects.all() if p.user == user]
     #     print(cart_product)
         if cart_product:
               for p in cart_product:
                   tempamount = (p.quantity * p.product_table.sell_price_usa)
                   Discount=(p.quantity * p.product_table.actual_price_usa)
                   amount += tempamount
                   dis += Discount
                   final_discount = dis
                   discount=amount-final_discount
                   final = (-discount)
                   if amount<=250:
                        totalamount = amount
                        shipping_amount = 0
                   else:
                         shipping_amount = 0
                         totalamount = amount + shipping_amount 
               return render(request,'usa/addtocart.html',{'dis':final,'discount':discount,'carts':cart ,'shipping_amount':shipping_amount,'totalamount':totalamount , 'amount':amount,'totalitem':totalitem})
         else:
              totalitem = 0
              if request.user.is_authenticated:
                    totalitem = len(Cart.objects.filter(user=request.user))
              return render(request,'usa/emptycart.html',{'totalitem':totalitem})

def plus_cart(request):
      if request.method == 'GET':
          prod_id = request.GET['prod_id']
          c = Cart.objects.get(Q(product_table=prod_id) & Q(user=request.user))
          c.quantity+=1
          c.save()
          amount = 0
          dis=0
          Discount=0
          cart_product = [p for p in Cart.objects.all() if p.user == request.user]
          for p in cart_product:
               tempamount = (p.quantity * p.product_table.sell_price_usa)
               Discount=(p.quantity * p.product_table.actual_price_usa)
               amount += tempamount
               dis += Discount
               final_discount = dis
               discount=amount-final_discount
               final = (-discount)
               if amount>=2000:  
                    totalamount = amount
                    shipping_amount = 0 
               else:
                    shipping_amount = 0
                    totalamount = amount + shipping_amount
          data = {
                 'quantity': c.quantity,
                 'amountusa': amount,
                 'totalamountusa': totalamount,
                 'shipping_amountusa':shipping_amount,
                 'discountusa':discount,
                 'disusa':final
            }
          return JsonResponse(data);

def minus_cart(request):
      if request.method == 'GET':
          prod_id = request.GET['prod_id']
          c = Cart.objects.get(Q(product_table=prod_id) & Q(user=request.user))
          c.quantity-=1
          c.save()
          amount = 0.0
          Discount=0
          dis=0
          cart_product = [p for p in Cart.objects.all() if p.user == request.user]
          for p in cart_product:
               tempamount = (p.quantity * p.product_table.sell_price_usa)
               Discount=(p.quantity * p.product_table.actual_price_usa)
               amount += tempamount
               dis += Discount
               final_discount=dis
               discount=amount-final_discount
               final = (-discount)
               if amount>=799:
                    totalamount = amount
                    shipping_amount = 0  
               else:
                    shipping_amount = 0
                    totalamount = amount + shipping_amount
          data = {
                 'quantity': c.quantity,
                 'amountusa': amount,
                 'totalamountusa': totalamount,
                 'shipping_amount':shipping_amount,
                 'discountusa':discount,
                 'disusa':final
            }
          return JsonResponse(data);

def remove_cart(request):
     if request.method == 'GET':
          prod_id = request.GET['prod_id']
          c = Cart.objects.get(Q(product_table=prod_id) & Q(user=request.user))
          c.delete()
          amount = 0.0
          amount = 0.0
          shipping_amount = 0.0
          discount=0.0
          dis=0.0
          final=0.0
          shipping_amount = 0
          cart_product = [p for p in Cart.objects.all() if p.user == request.user]
          for p in cart_product:
            tempamount = (p.quantity * p.product_table.sell_price_usa)
            Discount=(p.quantity * p.product_table.actual_price)
            amount += tempamount
            dis += Discount
            final_discount=dis
            discount=amount-final_discount
            final = (-discount)
          data = {
                 'amountusa': amount,
                 'totalamountusa': amount + shipping_amount,
                 'discountusa':discount,
                 'disusa':final
            }
          return JsonResponse(data)

def remove_wishlist(request):
     if request.method == 'GET': 
          prod_id = request.GET['prod_id']
          c = wishlist.objects.get(Q(product_table=prod_id) & Q(user=request.user))
          print(c)
          c.delete()
          return redirect('/wishlist')


@login_required(login_url='signin/')
def payment_done(request):
     custid=0
     user = request.user
     if request.method =="POST":
          custid = request.POST.get('custid')      
          payment_id = request.POST.get('payid')     
          order_id = request.POST.get('orderid')     
          signature = request.POST.get('signature')     
     Customer = customer.objects.get(id=custid)
     cart = Cart.objects.filter(user=user)
     for c in cart:
        orderPlaced(user=user,customer=Customer,razorpay_order_id=order_id,razorpay_signature=signature,razorpay_payment_id=payment_id,Total_price=c.total_cost, product_table=c.product_table, quantity=c.quantity).save()
        c.delete()
     ab= orderPlaced.objects.all()
     template=render_to_string('india/email_template.html',{'ab':ab})
     email= EmailMessage(
          'Thanks for Purchasing from Womens World',
          template,
          settings.EMAIL_HOST_USER,
          ['kailash.lodhi@gmail.com'],
     )
     email.fail_silently=False
     email.send()
     return redirect('order')

def invoice(request):
     totalitem = 0
     if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
     if request.method == "POST":
          abc = request.POST.get('order_id')
     ab = orderPlaced.objects.filter(user=request.user,id=abc)
     return render(request,'usa/invoice.html',{'totalitem':totalitem,'ab':ab})
