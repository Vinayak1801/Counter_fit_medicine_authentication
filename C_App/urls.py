"""Counterfeit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from C_App import views

urlpatterns = [
    path('',views.login,name='login'),
    path('logincode',views.logincode,name='logincode'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('mng_data',views.mng_data,name='mng_data'),
    path('deletequestion/<int:id>', views.deletequestion, name='deletequestion'),
    path('mng_data2',views.mng_data2,name='mng_data2'),
    path('add_product',views.add_product,name='add_product'),
    path('edit_prdt/<int:id>',views.edit_prdt,name='edit_prdt'),
    path('edit_product',views.edit_product,name='edit_product'),
    path('mng_prdt',views.mng_prdt,name='mng_prdt'),
    path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),
    path('mng_prdt2',views.mng_prdt2,name='mng_prdt2'),
    path('send_reply/<int:id>',views.send_reply,name='send_reply'),
    path('sendreply',views.sendreply,name='sendreply'),
    path('ver_distr',views.ver_distr,name='ver_distr'),
    path('accept_distributor/<int:id>',views.accept_distributor,name='accept_distributor'),
    path('accept_shop_req/<int:id>',views.accept_shop_req,name='accept_shop_req'),
    path('reject_shop_req/<int:id>',views.reject_shop_req,name='reject_shop_req'),
    path('reject_distributor/<int:id>',views.reject_distributor,name='reject_distributor'),
    path('ver_prdct',views.ver_prdct,name='ver_prdct'),
    path('accept_product/<int:id>',views.accept_product,name='accept_product'),
    path('reject_product/<int:id>',views.reject_product,name='reject_product'),
    path('ver_shop',views.ver_shop,name='ver_shop'),
    path('accept_shop/<int:id>',views.accept_shop,name='accept_shop'),
    path('reject_shop/<int:id>',views.reject_shop,name='reject_shop'),
    path('view_complnt',views.view_complnt,name='view_complnt'),
    path('view_rating',views.view_rating,name='view_rating'),
    path('distr',views.distr,name='distr'),
    path('dist_reg',views.dist_reg,name='dist_reg'),
    path('dist_stock/<int:id>',views.dist_stock,name='dist_stock'),
    path('stock_update_post',views.stock_update_post,name='stock_update_post'),
    path('dist_up_stock',views.dist_up_stock,name='dist_up_stock'),
    path('dist_up_stock_search',views.dist_up_stock_search,name='dist_up_stock_search'),
    path('dist_feedback',views.dist_feedback,name='dist_feedback'),
    path('dist_view_prdt',views.dist_view_prdt,name='dist_view_prdt'),
    path('dist_view_prdt_search',views.dist_view_prdt_search,name='dist_view_prdt_search'),
    path('dist_view_prdt2/<int:id>',views.dist_view_prdt2,name='dist_view_prdt2'),
    path('dist_view_req',views.dist_view_req,name='dist_view_req'),
    path('dist_view_req_search',views.dist_view_req_search,name='dist_view_req_search'),
    path('dist_view_req_stat',views.dist_view_req_stat,name='dist_view_req_stat'),
    path('shop_add_bill',views.shop_add_bill,name='shop_add_bill'),
    path('shop_add_bill1',views.shop_add_bill1,name='shop_add_bill1'),
    path('shop_add_bill2',views.shop_add_bill2,name='shop_add_bill2'),
    path('shop_add_bill2s',views.shop_add_bill2s,name='shop_add_bill2s'),
    path('finish_bill',views.finish_bill,name='finish_bill'),
    path('finish_bill1',views.finish_bill1,name='finish_bill1'),
    path('shop_view_product_bill/<int:id>',views.shop_view_product_bill,name='bill2'),
    path('bill2/<int:id>',views.bill2,name='bill2'),
    path('bill3',views.bill3,name='bill3'),
    path('addbill',views.addbill,name='addbill'),
    path('add_bill_post',views.add_bill_post,name='add_bill_post'),
    path('shop_shop',views.shop_shop,name='shop_shop'),
    path('shop_view_distri',views.shop_view_distri,name='shop_view_distri'),
    path('shop_view_distri1/<int:id>',views.shop_view_distri1,name='shop_view_distri1'),
    path('shop_view_distri2',views.shop_view_distri2,name='shop_view_distri2'),
    path('shop_view_feed',views.shop_view_feed,name='shop_view_feed'),
    path('shop_view_req',views.shop_view_req,name='shop_view_req'),
    path('block_unblock',views.block_unblock,name='block_unblock'),
    path('block_distributor/<int:id>',views.block_distributor,name='block_distributor'),
    path('unblock_distributor/<int:id>',views.unblock_distributor,name='unblock_distributor'),
    path('adddataset',views.adddataset,name='adddataset'),
    path('shop_reg',views.shop_reg,name='shop_reg'),
    path('shop_register',views.shop_register,name='shop_register'),
    path('search_prdt',views.search_prdt,name='search_prdt'),
    path('search_prdct',views.search_prdct,name='search_prdct'),
    path('search_complnt',views.search_complnt,name='search_complnt'),
    path('search_prdt_distri',views.search_prdt_distri,name='search_prdt_distri'),
    path('search_shop',views.search_shop,name='search_shop'),
    path('search_status_distri',views.search_status_distri,name='search_status_distri'),
    path('view_rating_distr',views.view_rating_distr,name='view_rating_distr'),
path('view_rating_distr_search',views.view_rating_distr_search,name='view_rating_distr_search'),
    path('shop_view_distrisearch',views.shop_view_distrisearch,name='shop_view_distrisearch'),
    path('shop_view_distri1search',views.shop_view_distri1search,name='shop_view_distri1search'),
    path('send_request_destr',views.send_request_destr,name='send_request_destr'),
    path('send_shop_request/<int:id>',views.send_shop_request,name='send_shop_request'),
    path('request_sent_shop',views.request_sent_shop,name='request_sent_shop'),
    path('logout',views.logout,name='logout'),


    path('andviewproducts',views.andviewproducts,name='andviewproducts'),
    path('userregistration',views.userregistration,name='userregistration'),
    path('logincode1',views.logincode1,name='logincode1'),
    path('sendfeedbackcode',views.sendfeedbackcode,name='sendfeedbackcode'),
    path('distributor_register',views.distributor_register,name='distributor_register'),
    path('dist_home',views.dist_home,name='dist_home'),




]
