from django.urls import path
from .views import service,serviceDetails,about,landing,contact,moreabout

urlpatterns = [
    path('landing/', landing, name='landing'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('serviceDetails/<int:pk>/',serviceDetails,name='serviceDetails'),
    path('about/', about, name='about'),
    path('moreabout/',moreabout,name='moreabout')
]
