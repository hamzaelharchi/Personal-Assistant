from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this

def index(request):
    return render(request, '/Home/index.html')


 
 
def recordings(request):
    if request.method == 'POST':
        data = request.get_json()
        print(f">>>>>>>>>>>>>>>{data}")
        answer = 'assistant.bot(str(voice_clip))'
        print(f'answer: {answer}')
        return {"answer": answer}

def register_req(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return render(request, 'Home/index.html')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="Home/register.html", context={"register_form":form})

def login_req(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request, 'Home/index.html')
			else:
				messages.error(request,"Invalid username or password.")
		else: 
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="Home/login.html", context={"login_form":form})

