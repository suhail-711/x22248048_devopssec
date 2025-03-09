from django.shortcuts import render
from django.contrib import messages
from .forms import UserSignUpForm

def signup_page(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, 'Account created')
            return redirect(signup_page)
    else:
        form = UserSignUpForm()
    return render(request,"users/signup.html",{'form':form})
