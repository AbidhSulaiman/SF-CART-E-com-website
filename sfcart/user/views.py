from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm


# Authentications

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        # Validate the form
        if form.is_valid():
            # Get cleaned data from form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            # Check if authentication was successful
            if user is not None:
                login(request, user)
                return redirect('products:product_main_page')
            else:
                form.add_error(None, 'Invalid username or password')  # Add error to form
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'user/user_login.html', context)


def user_logout(request):
    logout(request)