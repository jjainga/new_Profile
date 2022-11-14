# Create your views here.
import requests
from django.http import Http404, HttpResponse
from django.shortcuts import render


#need to map the url to this function
def index(request):
    repo_list = get_request(request)


    return render(
        request,
        'index.html',
         {
        'repos' : repo_list
         }
        )

def get_request(request):
    repo_list = requests.get("https://api.github.com/users/jjainga/repos").json
    return repo_list

def pdf_view(request):
    with open('./static/Joshua_Jainga_cv.pdf', 'rd') as pdf:
        try:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Dispostion'] = 'filename=Joshua_Jainga_cv.pdf'
            return response
        except FileNotFoundError:
            raise Http404()
    pdf.closed
