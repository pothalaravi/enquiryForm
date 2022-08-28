from django.urls import path
from EnquiryForm_App import views

urlpatterns =[
    path('create_data/',views.EnquiryView,name='create_data'),
]