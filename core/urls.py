from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name='core'
urlpatterns = [
path('',views.index,name='index'),
path('signin/',LoginView.as_view(template_name="core/signin.html"),name='signin'),
path('register',views.register,name='register'),
path('logout',views.logout_view,name='logout'),
path('categories',views.categories,name="categories"),
path('categories/<str:category_name>/',views.category,name='category'),
path('categories/<str:category_name>/<str:item_name>',views.item,name='item'),
path('add-to-bag/<int:item_id>',views.add_to_bag,name='add_to_bag'),
path('bag',views.bag_view,name="bag"),
path('search',views.search,name="search"),
path('order-details',views.order_details,name="order-details"),
path('edit-order-details',views.edit_order_details,name="edit-order-details"),
#path('order',views.order,name="order"),
path('add-order-details',views.add_order_details,name="add-order-details"),

]