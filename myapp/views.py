from django.shortcuts import render,redirect
from django.views.generic import View
from django import forms
from myapp.models import Products
from django.views.generic import CreateView,View,FormView,TemplateView,UpdateView,ListView,DetailView
from myapp.forms import RegisterForm,LoginForm,ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy



# Create your views here.



class SignUpView(CreateView):
    model=User
    template_name="register.html"
    form_class=RegisterForm
    success_url=reverse_lazy("signin")
    
    def form_valid(self,form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
    

class SigninView(FormView):
    model=User
    template_name="login.html"
    form_class=LoginForm

    # def get(self,request,*args,**kw):
    #     form=self.form_class
    #     return render(request,self.template_name,{"forms":form})


    def post(self,request,*args,**kw):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
        messages.error(request,"invalid credential")
        return render(request,self.template_name,{"forms":form})


class IndexView(ListView):
    template_name="index.html"
    model=Products
    context_object_name="products"
    
    # def form_valid(self, form):
    #     form.instance.user=self.request.user
    #     return super().form_valid(form)



class ProductCreateView(CreateView):
    template_name="product-add.html"
    form_class=ProductForm
    model=Products
    success_url=reverse_lazy("product-list")
    

class ProductDetailView(DetailView):
    model=Products
    template_name="detail.html"
    context_object_name="product"

class ProductUpdateView(UpdateView):
    model=Products
    template_name="productUpdate.html"
    form_class=ProductForm
    success_url=reverse_lazy("product-list")

class DeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Products.objects.get(id=id).delete()
        return redirect("product-list")