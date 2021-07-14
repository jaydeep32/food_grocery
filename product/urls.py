from django.urls import path
from product import views
from django.views.generic import TemplateView

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name='product/about.html'), name='about'),
    path('product/<str:slug>/', views.ProductDetail.as_view(), name='product-detail'),
]
