from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):

	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		my_user = User.objects.create_user(username, email, password)
		my_user.save()

		return redirect("success")

	return render(request, "backend/index.html")

def success(request):
	return render(request, "backend/success.html")