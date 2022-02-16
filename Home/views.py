from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def index(request):
    return render(request, 'Home/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created {username}!')
            return redirect('') #redirect to the home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def recordings(request):
    if request.method == 'POST':
        data = request.get_json()
        print(f">>>>>>>>>>>>>>>{data}")
        answer = 'assistant.bot(str(voice_clip))'
        print(f'answer: {answer}')
        return {"answer": answer}