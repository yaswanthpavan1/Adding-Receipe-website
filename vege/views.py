from django.shortcuts import  render , redirect
from .models import Recipe  # Using the Recipe model for CRUD operations
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required



# Home page view
def yash_page(request):
    return HttpResponse("<h1>This is yash website</h1>")

# Recipe listing and adding view
@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
        )
        return redirect('recipes')
    
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)


def delete_recipe(request, id):  
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image  # Make sure this is spelled correctly

        queryset.save()
        return redirect('recipes')  # Redirect after saving to avoid re-submission

    context = {'recipe': queryset}
    return render(request, "update_recipes.html", context)  # Correct template name and path



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        user = User.objects.filter(username=username).first()
        if user is None:
            messages.error(request, 'Invalid Username or Password')  # Combined error message
            return redirect('login_page')  # Use the URL name instead of hardcoding

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Username or Password')  # Combined error message
            return redirect('login_page')

        # Login the user
        login(request, user)
        messages.success(request, 'Successfully logged in.')  # Success message
        return redirect('recipes')  # Use the URL name instead of hardcoding
        
    return render(request, 'login.html')




def logout_page(request):
    logout(request)  # Logs out the user
    return redirect('/login/')  # Redirects to login page




def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')  # Use the URL name instead of hardcoding

        # Create the new user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password  # This method automatically hashes the password
        )

        messages.success(request, 'Account created successfully')
        return redirect('login_page')  # Use the URL name instead of hardcoding

    return render(request, 'register.html')


from django.http import HttpResponse

def csrf_failure(request, reason=""):
    return HttpResponse(f"CSRF verification failed: {reason}")
