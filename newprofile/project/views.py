# Create your views here.
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
import requests

# Create your views here.
#need to map the url to this function
def index(request):
    github_data = requests.get("https://api.github.com/users/jjainga/repos")
    repo_data = github_data.json

    return render(
        request,
        'index.html',
         {
        'repos' : repo_data
         }
        )


def pdf_view(request):
    with open('static/Joshua_Jainga_cv.pdf', 'rd') as pdf:
        try:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Dispostion'] = 'filename=Joshua_Jainga_cv.pdf'
            return response
        except FileNotFoundError:
            raise Http404()
    pdf.closed