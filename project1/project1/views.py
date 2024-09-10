from django.http import HttpResponse


def home(req):
    a=12
    b=13
    c=a+b
    print(c)
    return HttpResponse(c)