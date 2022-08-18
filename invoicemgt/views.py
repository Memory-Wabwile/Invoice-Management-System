from django.shortcuts import render , redirect
from .forms import InvoiceForm , InvoiceSearchForm, InvoiceUpdateForm
from .models import Invoice
from django.contrib import messages
# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab
# Create your views here.

def home(request):
    title = "welcome to Home page"
    context = {"title":title}

    return render (request , "home.html" , context)

def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    queryset = Invoice.objects.order_by('-invoice_date')[:6]
    total_invoices = Invoice.objects.count()

    if form.is_valid():
        form.save()
        messages.success(request , "Successfully Saved")
        return redirect('/list_invoice')
        
    context = {"form": form ,
                 "title": "New Invoice",
                 'queryset':queryset,
                 'total_invoices': total_invoices,
                 }

    return render (request , 'add_invoice.html' , context)

def list_invoice(request):
    title = "List of Invoices"
    queryset = Invoice.objects.all()
    
    form = InvoiceSearchForm(request.POST or None)
    context = { 
        "title" : title,
        "queryset" : queryset,
        "form" : form ,
    }

    if request.method == 'POST':
        queryset = Invoice.objects.filter(
                                    invoice_number__icontains=form['invoice_number'].value(), 
                                    name__icontains=form['name'].value()
                                    )
        context = { 
            "form" : form ,
            "title" : title,
            "queryset" : queryset,
    }
    return render (request , "list_invoice.html" , context)

def update_invoice(request,pk):
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)

    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_invoice')

    context = {
        'form': form
    }

    return render(request , 'add_invoice.html' , context)


def delete_invoice(request , pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_invoice')
    return render (request , 'delete_invoice.html')

# total_invoices = Invoice.objects.count()
# 