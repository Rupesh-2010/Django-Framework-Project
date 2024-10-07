from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    data= {
        'title' : 'Home Page',
        'BData' : 'Welcome Rupesh.',
        'CList' : ['PHP','JAVA','PYTHON','JS']
    }

    return render(request, "index.html", data)

def AboutUs(request):
    return HttpResponse("<b>Welcome To My Website</b>")

def contact(request):
    return HttpResponse("rups1808@gmai.com")

def contactDetails(request,contactid):
    return HttpResponse(contactid)