from django.shortcuts import render

# Create your views here.


def hello(request):
    
    classe= "Bonjour 5TWIN2"
    
    return render(request,'event/bonjour.html', {'c1':classe})
    

    