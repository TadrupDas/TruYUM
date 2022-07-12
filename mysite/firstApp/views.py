from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime,date
from .models import Menu,Cart
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def cart(request):
    return render(request,"cart.html")

def menu_admin(request):
    menu_items = Menu.objects.all();
    return render(request,'menu_admin.html',{'menu_items':menu_items})

def Edit_menu(request,id):    
    #
    menu_item = Menu.objects.get(id=id)
    #
    if request.method == "POST":
        item = Menu.objects.get(id=id)
        #getting data
        item_name = request.POST.get('name')
        item_price = request.POST.get('price')
        item_active = request.POST.get('active')
        item_dateoflaunch = datetime.strptime(request.POST.get('launch_date'), "%Y-%m-%d").strftime("%Y-%m-%d")
        item_category = request.POST.get('category')
        item_delivery = request.POST.get('free_delivery')

        # print(f"Item name - {item_name} its price {item_price} is active {item_active} category type {item_category} delivery {item_delivery} and date of launch {item_dateoflaunch}")
        
        if(item_name==None):
            messages.add_message(request, messages.ERROR, 'Required Item Name !')
            return redirect(f'/menu/admin/edit/{id}',{'menu_item':menu_item})
        elif(item_active==None):
            item_active = "No"
        elif(item_category==None):
            messages.add_message(request, messages.ERROR, 'Required Item Category !')
            return redirect(f'/menu/admin/edit/{id}',{'menu_item':menu_item})
        elif(item_delivery==None):
             item_delivery = "No"
        elif(item_dateoflaunch==None):
            messages.add_message(request, messages.ERROR, 'Required Item Date of Launch !')
            return redirect(f'/menu/admin/edit/{id}',{'menu_item':menu_item})
        
        item.name = item_name
        item.price = item_price
        if(item_active=="Yes"):            
            item.active = True
        else:
            item.active = False        
        item.date_of_launch = item_dateoflaunch
        if(item_delivery=="Yes"):            
            item.free_delivery = True
        else:
            item.free_delivery = False
        item.category_type = item_category
        item.save()
        
        return redirect('/menu/admin/edit/status')
    
    #Normal Render
    return render(request,'Edit_menu.html',{'menu_item':menu_item})

def menu_item_status (request):
    return render(request,"edit_menu_admin_status.html")

def logout (request):
    auth.logout(request)
    return redirect('/signin')

@login_required(login_url='signin')
def menu_customer (request):
    menu_items = Menu.objects.filter(active=True, launch_date__lte=date.today())
    return render(request,'menu_customer.html',{'menu_items':menu_items})

@login_required(login_url='signin')
def cart_list_customer (request):
    carts = Cart.objects.filter(user_id=request.user)
    print(carts)
    return render(request,'cart.html',{'carts':carts})


@login_required(login_url='signin')
def cart_list_customer_add (request,id,name,delivery,price,category):
    #
    carts = Cart.objects.filter(user_id = request.user)
    #
    current_user = request.user
    cart_object = Cart()
    cart_object.user_id = current_user
    cart_object.name = name
    cart_object.price = price
    if(delivery == 'False'):
        cart_object.delivery_free=False
    else:
        cart_object.delivery_free=True
        
    cart_object.category_type=category
    cart_object.save()
    
    messages.info(request,'Item added to cart successfully')
    return redirect('/customer/cart',{'carts':carts})

@login_required(login_url='signin')
def delete_cart_item(request,id):
    cart_obj = Cart.objects.filter(user_id=request.user,id=id)
    # print(cart_obj)
    cart_obj.delete()
    messages.info(request,"Item removed from cart successfully !")
    return redirect('/customer/cart')
    



