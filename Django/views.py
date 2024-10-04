from django.http import HttpResponse

def AboutUs(request):
    return HttpResponse("Welcome To My Website")

def contact(request):
    return HttpResponse("rups1808@gmai.com")
