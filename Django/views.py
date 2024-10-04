from django.http import HttpResponse

def AboutUs(request):
    return HttpResponse("<b>Welcome To My Website</b>")

def contact(request):
    return HttpResponse("rups1808@gmai.com")
