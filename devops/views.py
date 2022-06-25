from django.http import HttpResponse
 
 
def index(request):
  return HttpResponse("<h1>na here we gather dey!</h1>")