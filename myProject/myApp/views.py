from django.shortcuts import render

# Create your views here.
def all_myApp(request):
    return render(request, 'myApp/all_myApp.html')
