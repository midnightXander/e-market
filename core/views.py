from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Item,Category,Item_in_bag,Order_details
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from itertools import chain
from .forms import Order_details_form

def index(request):
    """the home page"""
    items = Item.objects.all()
    
    context = {'items':items} 
    return render(request,"core/index.html",context)

def category(request,category_name):
    category = Category.objects.get(name=category_name)
    items = Item.objects.filter(category=category)

    context = {'items':items}
    return render(request,"core/category.html",context)  

def item(request,item_name,category_name):
    category = Category.objects.get(name=category_name)
    item = Item.objects.get(name=item_name)
    
    context = {'item':item,'category':category}
    return render(request,"core/item.html",context)

def register(request):
    
    if request.method != "POST":
        """submit blank form"""
        form = UserCreationForm()
    
    else:
        """process data"""
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request,authenticated_user)

            return HttpResponseRedirect(reverse("core:index"))

    context={"form":form}
    return render(request,"core/register.html",context)

def categories(request):

    categories = Category.objects.all()
    context = {"categories":categories}

    return render(request,"core/categories.html",context)


def logout_view(request):
    """logout the user"""
    logout(request)
    return HttpResponseRedirect(reverse("core:index"))

def add_to_bag(request,item_id):
    username = request.user.username

    item = Item.objects.get(id=item_id)

    check_item_in_bag = Item_in_bag.objects.filter(item_id=item_id,username=username).first()

    if check_item_in_bag == None:
        new_item_in_bag = Item_in_bag.objects.create(item_id=item_id,username=username)
        new_item_in_bag.save()
        
        return HttpResponseRedirect(reverse("core:index"))
    
    else:
        check_item_in_bag.delete()
        return HttpResponseRedirect(reverse("core:index"))


    return redirect("/")

def bag_view(request):
    username = request.user.username
    items_count = 0
    items_in_bag = Item_in_bag.objects.filter(username=username)
    item_ids = []
    items_all = []
    for item in items_in_bag :
        item_ids.append(item.item_id)
    
    for item_id in item_ids :
        items = Item.objects.get(id = item_id)
        items_all.append(items) 
    
    items_count = len(items_in_bag)    

    context = {"items":items_all,"items_count":items_count}
    return render(request,"core/bag.html",context)

def search(request):
    """search for an item"""

    if request.method == "POST":
        item_name = request.POST['item_name']
        search_items = Item.objects.filter(name__icontains = item_name)
             
    context = {"search_items":search_items,"item_name":item_name}
    return render(request,"core/search.html",context)    

def add_order_details(request):
    """add details for placing orders"""
    user = request.user
    if request.method != "POST":
        """generate empty form"""
        form = Order_details_form()

    else:
        """process data"""
        form = Order_details_form(data=request.POST) 
        if  form.is_valid():
            new_order_detail = form.save(commit=False)
            new_order_detail.owner = user
            new_order_detail.save()
            
        return HttpResponseRedirect(reverse("core:index"))

    context = {"form":form}
    return render(request,"core/add_order_details.html",context)     

def edit_order_details(request):
    """edit details for placing an order"""

    order_details = Order_details.objects.get(owner=request.user)
    if request.method != "POST":
        """generate prefill form by current user"""
        form = Order_details_form(instance = order_details)

    else:
        """process data"""
        form = Order_details_form(data=request.POST,instance=order_details)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse("core:index"))    

    context = {"form":form}
    return render(request,"core/edit_order_details.html",context)

def order_details(request):
    """show edtails for placing orders"""
    order_details = Order_details.objects.get(owner=request.user)
    
    context={"order_details":order_details}
    return render(request,"core/order_details.html",context)

#def order(request):

