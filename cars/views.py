from django.shortcuts import render, get_object_or_404
from .models import Car, Photo

def cars(request):
    cars = Car.objects.order_by('-created_date')
    car_with_main_photo = []
    for car in cars:
        main_photo = Photo.objects.filter(truck=car, is_main=True).first()
        car_with_main_photo.append((car, main_photo))
    print(car_with_main_photo)
    if not car_with_main_photo:
        main_photo = Photo.objects.first()
        car_with_main_photo = [(car, main_photo) for car in cars]
    print(car_with_main_photo)
    data = {
        'car_with_main_photo': car_with_main_photo,
        'cars': cars,    
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    fields = single_car._meta.get_fields()
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)

def search(request):
    cars = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    car_with_main_photo = []

    for car in cars:
        main_photo = Photo.objects.filter(truck=car, is_main=True).first()
        if main_photo:
            car_with_main_photo.append((car, main_photo))
        else:
            first_photo = car.truck_photos.first()
            if first_photo:
                car_with_main_photo.append((car, first_photo))

    data = {
        'cars_with_main_photo': car_with_main_photo, 
    }

    return render(request, 'cars/search.html', data)
