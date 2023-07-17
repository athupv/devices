

from django.shortcuts import render, redirect
from .models import Car

# def car_list(request):
#     cars = Car.objects.all()
#     return render(request, 'car_list.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        make = request.POST.get('make')
        model = request.POST.get('model')
        year = request.POST.get('year')
        color = request.POST.get('color')
        mileage = request.POST.get('mileage')
        price = request.POST.get('price')

        car = Car(make=make, model=model, year=year, color=color, mileage=mileage, price=price)
        car.save()
        return redirect('add_car')

    return render(request, 'add_car.html')
