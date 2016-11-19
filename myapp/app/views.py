from django.shortcuts import render

# Create your views here.

def home(req):
    names = ['basha', 'baji', 'kumar', 'raja', 'srikanth']
    context = { "users": names}
    return render(req, "users.html", context)
