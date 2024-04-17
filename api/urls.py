# api/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('user-login/', views.user_login, name='user_login'),
    path('admin-signup/', views.admin_signup, name="admin_signup"),
    path('user-signup/', views.user_signup, name="user_signup"),
    path('admin-page/',views.register_product, name='admin_page'),
    path('user-page', views.verify_product, name='user_page'),
    path('verify/', views.verify_qr_code_process, name='verify_qr_code_process'),
    path('product_list',views.product_list,name='product_list'),
    path('product_info/<str:name>/<str:brand>/<str:price>/<str:manufacturer_id>/<str:product_sn>/', views.product_info_page, name='product_info_page'),
     path('delete/', views.delete_products, name='delete_products'),
        # Add other URL patterns as needed
]


