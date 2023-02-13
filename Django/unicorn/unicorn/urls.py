from django.contrib import admin
from django.urls import path, re_path, include
from feed import views

catalog_patterns = [
    path('', views.catalog),
    path('new/', views.new),
    path('top/', views.top),
]

product_patterns = [
    path('', views.product),
    path('comments/', views.comments),
    path('questions/', views.questions),
]

profile_patterns = [
    path('', views.profile),
    path('<str:name>/<int:age>/', views.profile),
    path('<str:name>/', views.profile),
]

urlpatterns = [
    path('', views.index, name='feed'),
    re_path(r'^contact', views.contact, name='contact'),
    re_path(r'^about', views.about, name='about'),
    path('profile/', views.profile),
    path('products/', include(catalog_patterns)),
    path('product/<int:id>/', include(product_patterns)),

    path('reg/setting/', views.set_cookies),
    path('get', views.get_cookies),

    path('data/', views.data, name='data'),
    path('admin/', admin.site.urls),
    path('reg/', views.registration)

]
