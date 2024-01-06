from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Car, CustomUser

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            CustomUser.objects.create_user(username = username, password = password)
            return redirect('login')  
        else:
            error_message = "Passwords do not match."
            return render(request, 'registration.html', {'error_message': error_message})

    return render(request, 'registration.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)


        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            return render(request, 'login.html') 
        else:
            login(request, user)
            return redirect('addcar')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def add_car(request):
    if(request.method == 'POST'):
        company=request.POST['company']
        brand=request.POST['brand']
        model=request.POST['model']
        number=request.POST['number']
        data=Car(company=company, brand=brand, model=model, number=number)
        data.save()
    return render(request ,'addcar.html')

    
@login_required
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    car.delete()

    return redirect('carlist')




@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':

        car.brand = request.POST.get('brand', '')
        car.company = request.POST.get('company', '')
        car.model = request.POST.get('model', '')
        car.number = request.POST.get('number', '')
        
        car.save()

        return redirect('carlist')

    return render(request, 'edit_car.html', {'car': car})
