from math import ceil
from urllib import request, response
from django.shortcuts import render,redirect
from shop.models import OrderUpdate, contact,Product,Orders
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    allprods=[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n=len(prod)
        nslides = n//4+ ceil ((n/4) - (n//4))
        allprods.append([prod,range(1,nslides),nslides])
        params={'allprods':allprods}






    return render(request,"index.html",params)
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        pnumber=request.POST.get('pnumber')
        # if not all(myquery=[name, email, desc, pnumber]):
        myquery=contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
    messages.info(request,"we'll get back to you soon")
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def checkout(request):
     if not request.user.is_authenticated:
         messages.warning(request,"login and try again")
         return redirect('/auth/login')
     if request.method=="POST":
         items_json =request.POST.get('itemsjson','')
         name =request.POST.get('name','')
         amount=request.POST.get('amt','')
         email=request.POST.get('email','')
         address1=request.POST.get('address1','')
         address2=request.POST.get('address2','')
         city=request.POST.get('city','')
         zipcode=request.POST.get('state','')
         phone=request.POST.get('zip_code','')
         order=request.POST.get('phone','')
         order=Orders(items_json=items_json,name=name,amount=amount,email=email,address1=address1,address2=address2,city=city,zipcode=zipcode,phone=phone,order=order)
         print(amount)
         Orders.save()
         update=OrderUpdate(order_id=Orders.order_id,update_desc="the order has been saved")
         update.save()
         thank=True


# ## Payment integration starts from here
# order = Orders.objects.get(id=1)  # Fetch an order from the database
# id = order.order_id 
# oid=str(id)+"ShopyCart"
# # param_dict={

# # 'ORDER_ID'==oid,
# # 'TXN_AMOUNT'==str(amount),
# # 'CUST_ID'==email,
# # 'INDUSTRY_TYPE_ID'=='Retail',
# # 'WEBSITE'=='WEBSTAGING',
# # 'CHANNEL_ID'=='WEB',
# # 'CALLBACK_URL'=='http://127.0.0.1:8000/handlerequest/',

# # }

# # param_dict['CHECKSUMHASH']=checksum.generate_checksum
# # (param_dict,MERCHANT_KEY):return render(request,"checkout.html") # type: ignore
# def checkout_view(request):
#     param_dict = {
#         "ORDER_ID": "12345",
#         "CUST_ID": "customer_001",
#         "TXN_AMOUNT": "500.00",
#         # Add other parameters as needed
#     }
#     MERCHANT_KEY = "YourMerchantKey"

#     return render(request, "checkout.html", {"param_dict": param_dict, "MERCHANT_KEY": MERCHANT_KEY})  # type: ignore

# @csrf_exempt
# def handlerequest(request):
#     #paytm will send you post request here
#     form =request.POST
#     response_dict={}
#     for i in form.keys():
#         response.dict[i] = form [i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

# verify = checksum.Veriy_checksum(response.dict,MERCHANT_KEY,checkum)
# if verify:
#     if response_dict['RESPCODE'] == '01':
#         print('order successful')
#         a=response.dict['ORDERID']
#         b=response.dict['TXNAMOUNT']
#         rid=a.replace("ShopyCart","")

#         print(rid)
#         filter2=Orders.objects.filter(order_id=rid)
#         print(rid)
#         filter2= Orders.objects.filter(order_id=rid)
#         print(filter2)
#         print(a,b)
#         for post1 in filter2:
#             post1.odd=a
#             post1.amountpaid=b
#             post1.paymentstatus="PAID"
#             post1.save()
#         print("run agede function")
#     else:
        
#         print('order was not successful because' + response.dict ['RESPMSG'])
# def payment_status_view(request):
#     return render(request, 'paymentstatus.html')
def myprofile(request):


    if not request.user.is_authenticated:
        messages.warning(request,"login and try again")

        return redirect('/auth/login')
    currentuser=request.user.username
    items=Orders.objects.filter(email=currentuser)
    for i in items:
        print(i.oid)
        rid=myid.replace("ShopyCart","") # type: ignore
        print(rid)
        status=OrderUpdate.objects.filter(order_id=int(rid))
        print(status)
    context={"items":items,"status":status}
    print(currentuser)
    return render(request,"myprofile.html")
              
 