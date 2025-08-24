from django.shortcuts import render
from .models import myUsers
from django.shortcuts import get_object_or_404

# Create your views here.
def all_myApp(request):
    #now the myUsers that i created i wanna see that to my frontend as well so for that i need to create views for that as well
    users = myUsers.objects.all
    return render(request, 'myApp/all_myApp.html', {'users':users})

def user_discription(request, user_id):
    users = get_object_or_404(myUsers, pk = user_id) # get user discription from DB using the userid
    return render(request, 'myApp/user_discription.html', {'users': users})

def user_forms(request):
    return render(request, 'myApp/user_forms.html')