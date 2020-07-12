from django.shortcuts import render,redirect
from .models import Storemodel
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


#Code for the creation of views
def home(request):
    return render(request,'homestore.html')


def storeitems(request):
    store = Storemodel.objects.all().order_by('date')
    return render(request,'store_list.html',{'store':store})


def store_create(request):
    if request.method == 'POST':
        form = forms.CreateStoreItem(request.POST,request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            #instance.save()
            return redirect('store:storeit')
    else:
        form = forms.CreateStoreItem()
    return render(request,'store_create.html',{'form':form })
