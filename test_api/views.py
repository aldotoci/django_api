from django.http import JsonResponse
import requests

def search(request):
    keyword = request.GET.getlist("keyword")[0]
    r = requests.get('https://gogoanime-api-flask.vercel.app/api/search/' + keyword)
    r = r.json()
    print(request.GET.getlist("keyword")[0])
    return JsonResponse(r, safe=False)

def category(request):
    id = request.GET.getlist("id")[0]
    r = requests.get('https://gogoanime-api-flask.vercel.app/api/anime/' + id)
    r = r.json()
    print(id)
    return JsonResponse(r, safe=False)

def watch(request):
    id = request.GET.getlist("id")[0]
    ep = request.GET.getlist("ep")[0]
    r = requests.get('https://gogoanime-api-flask.vercel.app/api/watch/' + id + '/' + ep)
    r = r.json()
    print(id)
    return JsonResponse(r, safe=False)

def genre(request):
    genre_s = request.GET.getlist("genre")[0]
    page = request.GET.getlist("page")[0]
    r = requests.get('https://gogoanime-api-flask.vercel.app/api/genre/' + genre_s + '/' + page)
    r = r.json()
    return JsonResponse(r, safe=False)
def recent(request):
    page = request.GET.getlist("page")[0]
    r = requests.get('https://gogoanime-api-flask.vercel.app/api/recent?number=' + page)
    r = r.json()
    return JsonResponse(r, safe=False)
