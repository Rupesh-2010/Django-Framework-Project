from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    # data= {
    #     'title' : 'Home Page',
    #     'BData' : 'Welcome Rupesh.',
    #     'CList' : ['PHP','PYTHON','JS'],
    #     'Num' : [10,20,30,40,50,44,32],
    #     'Student_Num' : [
    #         {'Name': 'Rupesh', 'Phone': 7083323315},
    #         {'Name': 'Anjali', 'Phone': 9552425195}
    #         ]
    # }

    return render(request, "contact")

def contact(request):
    return HttpResponse("index.html")

def AboutUs(request):
    return HttpResponse("<b>Welcome To My Website</b>")

def contact(request):
    return HttpResponse("rups1808@gmai.com")

def contactDetails(request,contactid):
    return HttpResponse(contactid)