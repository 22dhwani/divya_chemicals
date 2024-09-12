from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home,name="home"),
     path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('services/',views.servicess,name="services"),
    path('products/<str:pk>/',views.products,name="products"),
    path('blogs/',views.blogs,name="blogs"),
    path('clientele/',views.clientele,name="clientele"),
    path('home/',views.querySet,name='contactQuery')
    ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)