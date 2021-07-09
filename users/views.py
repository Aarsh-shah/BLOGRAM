from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
# Create your views here.
def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			messages.success(request, f'Welcome {username}')
			form.save()
			return redirect('login')

	else:
		form = UserRegisterForm()


	return render(request, 'users/register.html',{ 'form':form })

@login_required
def profile(request):
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST,instance= request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
		tempname=request.user.username
		tempemail=request.user.email
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()

			messages.success(request, f' Your ac has been Updated from {tempname} to {request.user.username}')
			messages.success(request, f' Your ac has been Updated from {tempemail} to {request.user.email}')
			messages.success(request, f' Your profile pic is also up to date')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance= request.user)
		p_form=ProfileUpdateForm(instance= request.user.profile)
	context = {
	'p_form':p_form,
	'u_form':u_form
	}

	
	return render(request, 'users/profile.html',context)