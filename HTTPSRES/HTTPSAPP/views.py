from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def myfirstmsg1(request):
    msg="hello sakshi students"
    return HttpResponse(msg)