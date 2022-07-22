from django.http import HttpResponse

def demo(request):
    return HttpResponse('Welcome Docker')

def welcome(request):
    return HttpResponse('Welcome Docker Docker working.........1')
