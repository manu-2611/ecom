from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]























#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index,name='Home'),
#     path('about/', views.about,name='AboutUs'),
#     path('contact/', views.contact,name='ContactUs'),
#     path('tracker/', views.tracker,name='TrackingStatus'),
#     path('search/', views.search,name='Search'),
#     path('products/<int:id>', views.productView, name='productView'),
#     path('checkout/', views.checkout,name='checkout'),
# ]
