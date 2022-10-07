from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.product_list),
    path('<int:pk>/', views.product_detail),
    path('<int:pk>/reviews/', include('product_reviews.urls')) # localhost:8000/api/products/id/reviews/
]