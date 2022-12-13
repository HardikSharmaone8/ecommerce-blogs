import json

from django.shortcuts import render
from django.http import HttpResponse

from .models import Items,Contacts,Checkout,Tracker
from math import ceil

# Create your views here.
def show_shop(request):
    allPro = []
    proCat = Items.objects.values("category")
    print(proCat)
    cats = {item['category'] for item in proCat}
    print("Value of cats is",cats)

    for cat in cats:
        prod= Items.objects.filter(category=cat)
        print("value if prod",prod)
        n=len(prod)
        print("Length of n is",n)
        nslide = n//4 + ceil((n/4) - (n//4))
        allPro.append([prod,range(1,nslide),nslide])


    params = {"allProduct" : allPro}
    print("value of partams is:",params)
    print("value of all product list",allPro)
    return render(request,'shop/index.html', params)


#searched item not found in cart logic
def not_found(request):
    return (request,'notfound.html')


#Search box logic
def search_matching(get_searched_product,item):
    if get_searched_product in item.product_name.lower() or get_searched_product in item.desc.lower() or get_searched_product in item.category.lower():
        print("values get Suceesfully")
        return True
    else:
        return False

def search(request):
    get_searched_product = request.GET.get('search','')
    print("searching product is",get_searched_product)
    allPro = []
    proCat = Items.objects.values("category")
    print(proCat)
    cats = {item['category'] for item in proCat}
    print("Value of cats is",cats)

    for cat in cats:
        prods= Items.objects.filter(category=cat)

        print("value if prod",prods)
        prod = [item for item in prods if search_matching(get_searched_product,item)]
        n=len(prod)
        print("Length of n is",n)
        nslide = n//4 + ceil((n/4) - (n//4))
        if len(prod) != 0:
            allPro.append([prod,range(1,nslide),nslide])


    params = {"allProduct" : allPro}
    print("value of partams is:",params)
    print("value of all product list",allPro)

    #if no products searched in kart than length of allProduct in zero
    if len(allPro) == 0:
        return render(request,'shop/notfound.html')
    return render(request,'shop/index.html', params)

def product_view(request,myid):
    productview = Items.objects.filter(id=myid)
    print(productview)
    params = {"productPreview" : productview,}
    return render(request,'shop/productview.html',params)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('description','')
        contact = Contacts(Name=name,Email=email,Phone=phone,desc=desc)
        contact.save()
        check_contact = True
        return render(request, "shop/contacts.html", {"check_contact": check_contact})

    return render(request,"shop/contacts.html",)

def checkout(request):
    if request.method == "POST":
        product = request.POST.get('product_json','')
        order_id = request.POST.get('order_id','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')+" "+request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        pincode = request.POST.get('pincode','')
        phone = request.POST.get('phone','')

        get_customer_address = Checkout(Product=product,OrderId=order_id,Name=name,Email=email,Address=address,City=city,State=state,Pincode=pincode,Phone=phone)
        get_customer_address.save()

        customer_order_id = Tracker(OrderId=order_id,Description='Order Is place Successfully')
        customer_order_id.save()

        check = True
        return render(request,"shop/checkout.html",{"check":check})
    return render(request,"shop/checkout.html")

def tracker(request):
    if request.method == "POST":
        customer_order_id = request.POST.get("customer_order_id",'')
        print("customer order id",customer_order_id)
        try:
            order_status = Checkout.objects.filter(OrderId=customer_order_id)
            print("OrderStatus",order_status)

            if len(order_status) > 0:
                update = Tracker.objects.filter(OrderId=customer_order_id)
                print("UPdation",update)
                updates = []
                for item in update:

                    product_name_value = []
                    product_names_values = []

                    for items in order_status:
                        length_of = len(list(json.loads(items.Product).values()))
                        for i in range(length_of):
                            product_name_value.append(list(json.loads(items.Product).values())[i][1])

                    for itemss in order_status:
                        length_of = len(list(json.loads(itemss.Product).values()))
                        for i in range(length_of):
                            product_names_values.append(list(json.loads(itemss.Product).values())[i][0])

                    updates.append([item.Description, item.Date, product_name_value, product_names_values])

                    print("updates",updates)
                    print("kjhsdafsad", product_name_value)

                return render(request,'shop/tracker.html',{"updates":updates})

            else:
                return HttpResponse("Not A valid Tracking Details..")
        except Exception:
            return HttpResponse("Error Occure While Fetching the Tracking Details")



    return render(request,"shop/tracker.html")


