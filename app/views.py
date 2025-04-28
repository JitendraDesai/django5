from django.shortcuts import render

# Create your views here.
import json
file=open(r'D:\Django\django5\app\car.json','r')
# file=open(r'E:\templates_inheritance\App\recipes.json','r')
json_data=file.read()
py_data=json.loads(json_data)

cars=py_data["cars"]

def Home(request):
    context={
        'cars' : cars,
    }
    return render(request, 'home.html', context)


def Cars(request, id):
    context={
        'car' : cars[id - 1],
    }
    return render(request, 'index.html',context)

def About(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')