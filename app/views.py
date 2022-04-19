from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'home.html')    

def generate_pwd(request):
    import secrets
    import string

    # secure random string
    secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(8)))
    print(secure_str)
    # Output QQkABLyK

    # secure password
    password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
    # print(password)
    # output 4x]>@;4)
    context = { 'pwd':password}

    return render(request, template_name='output.html', context=context)