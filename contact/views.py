from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from contact.filters import ContactFilter

from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import *


def index(request):  
    if request.user.is_anonymous:
        print(request)
        
        return redirect("login")
    return render(request,'index.html')

def registerUser(request):  

	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')

		else:
			form = UserCreationForm()
		context = {'form':form}
		return render(request, 'register.html', context)

def logoutUser(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def loginUser(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username or password is incorrect')

		return render(request, 'login.html')


@login_required(login_url='login')
def dashboard(request):
	contacts = Contact.objects.all()
	filter = ContactFilter(request.GET, queryset=Contact.objects.all())
	contacts = filter.qs
	p = Paginator(contacts, 4)  
	page_number = request.GET.get('page')
	page_obj = p.get_page(page_number) 
	context= {'contacts': contacts, 'page_obj': page_obj, 'filter': filter}
	return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def filter(request):
	contacts = Contact.objects.all()
	f = ContactFilter(request.GET, queryset=contacts)
	context= {'filter': f}
	return render(request, 'dashboard.html', context)
	

@login_required(login_url='login')
def createContact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		
		if form.is_valid():
			form.save()
			messages.info(request, 'Contact successfully created')
			return redirect('/createContact')

		context = {'form':form}
		return render(request, 'contact_form.html', context)
	context = {'form':form}
	return render(request, 'contact_form.html',context)

@login_required(login_url='login')
def viewContact(request, pk):
	order = Contact.objects.filter(id=pk)
	context = {'form': order}
	return render(request, 'contact_details.html', context)

@login_required(login_url='login')
def updateContact(request, pk):

	contact = Contact.objects.get(id=pk)
	form = ContactForm(instance=contact)
	
	if request.method == 'POST':
		print(request.POST)
		form = ContactForm(request.POST, instance=contact)
		if form.is_valid():
			form.save()
			messages.info(request, 'Contact successfully updated')
			return redirect("/updateContact/<int:pk>")
		else:
			print("eroor in saving")
		
	context = {'form':form}
	return render(request, 'update_contact.html', context)

@login_required(login_url='login')
def deleteContact(request, pk):
	contact = Contact.objects.get(id=pk)
	if request.method == "POST":
		contact.delete()
		# messages.info(request, 'Contact successfully deleted!!')
		return redirect('/')

	context = {'contact':contact}
	return render(request, 'delete_contact.html', context)