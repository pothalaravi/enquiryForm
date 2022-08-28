
from django.shortcuts import render
from EnquiryForm_App.models import Enquiry
from EnquiryForm_App.forms import EnquiryForm
from django .http import  HttpRequest

def EnquiryView(request):

    if request.method=='POST':
        pass
    else:
        form = EnquiryForm()
        context ={
            "form": form
        }
        return render (request,'enquiry_form.html',context)






