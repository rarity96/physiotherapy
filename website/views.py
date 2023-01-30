from django.shortcuts import render, redirect
from django.views import View
from .models import *
import random


# Create your views here.

def get_random_customers(customers):
    list_of_customers = list(customers)
    if len(list_of_customers) >= 3:
        random.shuffle(list_of_customers)
        first_customer = list_of_customers[0]
        second_customer = list_of_customers[1]
        third_customer = list_of_customers[2]
        ctx = {'customers': customers,
               'first_customer': first_customer,
               'second_customer': second_customer,
               'third_customer': third_customer}
        return ctx
    else:
        return {}


class Home(View):
    template_name = 'index.html'

    def get(self, request):
        customers = Customer.objects.all()
        ctx = get_random_customers(customers)
        return render(request, self.template_name, ctx)


class Contact(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if not fname or not lname or not email or not subject or not message:
            error_text = "You need to fill all things before submit"
            ctx = {'error_text': error_text}
            return render(request, self.template_name, ctx)
        add_message = Message.objects.create(first_name=fname, last_name=lname, email=email,
                                             subject=subject, message=message)
        success_message = "Thank you for your message, we will contact you as soon as possible"
        ctx = {"success_message": success_message}
        return render(request, self.template_name, ctx)


class Blog(View):
    template_name = 'blog.html'

    def get(self, request):
        return render(request, self.template_name)


class BlogSingle(View):
    template_name = 'blog-single.html'

    def get(self, request):
        return render(request, self.template_name)


class Services(View):
    template_name = 'services.html'

    def get(self, request):
        customers = Customer.objects.all()
        ctx = get_random_customers(customers)
        return render(request, self.template_name, ctx)


class About(View):
    template_name = 'about.html'

    def get(self, request):
        employees = Employee.objects.all()
        ctx = {'employees': employees}
        return render(request, self.template_name, ctx)
