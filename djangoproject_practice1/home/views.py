from django.shortcuts import render,redirect
from .models import *

# Create your views here.



def home(request):
    if request.method == "POST":
        data = request.POST
        movie_card = request.FILES.get('movie_card')
        movie_title = data.get('movie_title')
        movie_details = data.get('movie_review')


        Movie.objects.create(
            movie_card = movie_card,
            movie_title = movie_title,
            movie_details = movie_details,
            )
        return redirect('/')
    queryset = Movie.objects.all()

    if request.GET.get('search'):
        queryset =queryset.filter(movie_title__icontains = request.GET.get('search'))

    context = {'movies':queryset}
    return render(request,"./home.html",context)



def update(request,id):
    queryset = Movie.objects.get(id = id)
    if request.method == "POST":
        data =request.POST
        movie_card = request.FILES.get('movie_card')
        movie_title = data.get('movie_title')
        movie_details = data.get('movie_review')


        queryset.movie_title = movie_title
        queryset.movie_details = movie_details

        if movie_card:
            queryset.movie_card = movie_card
        queryset.save()
        return redirect('/')
    context = {'movie':queryset}
    return render(request,"update.html",context)


def delete(request,id):
    queryset = Movie.objects.get(id = id)
    queryset.delete()
    return redirect('/')