from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name= 'home'),
    path('contact.html',views.contact, name= 'contact'),
    path('about.html',views.about, name= 'about'),
    path('blog.html',views.blog, name= 'blog'),
    path('blog_details.html',views.blog_detail, name= 'blog_details'),
    path('pricing.html',views.pricing, name= 'pricing'),
     path('service.html',views.service, name= 'service'),
     path('appointment.html',views.appointment, name= 'appointment'),
    
]