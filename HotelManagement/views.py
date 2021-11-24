from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import requests
from string import ascii_lowercase, ascii_uppercase, digits
from random import choices
# Create your views here.


def home(request):
    return render(request, 'HotelManagement/index.html')

def register(request):
    if request.method == "POST":
        Name = request.POST.get('Name', '')
        Email = request.POST.get('Email', '')
        phone_num = request.POST.get('PhoneNo','')
        PWD = request.POST.get('PWD', '')
        print(Email)

        random_str = "".join(choices(ascii_uppercase + ascii_lowercase + digits, k=6))

        url = "https://email-sender1.p.rapidapi.com/"

        querystring = {"txt_msg":"test of the body","to":Email, "from":"Team 20","subject":"Greetings","html_msg":f"<html><body><b>Hello, {Name}</b><br>{random_str}</body></html>"}

        headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "email-sender1.p.rapidapi.com",
        'x-rapidapi-key': "f4a006106dmshc46a4e2a30f153dp1a2d06jsn7506f81db2ee"
        }

        payload = """{\r
                      \"key1\": \"value\",\r
                      \"key2\": \"value\"\r
                     }"""

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        print(response.text)

        # print(type(Email))
        # Reg = User(name = Name, )
    return render(request, 'HotelManagement/register.html')