from django.http import HttpResponse

# Create your views here.

#HTTp Request
# tem que ter o paramentro (request) para ter, o clinte recebar o returno de http response.


def home (request):
    return HttpResponse("Home 1")
    #return HTTP Response
def contato(request):
    return HttpResponse("Contato teste")
  
def sobre(request):
    return HttpResponse("Sobre teste")