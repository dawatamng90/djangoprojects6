from django.shortcuts import render,redirect
from testapp.forms import MovieForm
from testapp.models import Movie

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def addmovie_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Record inserted into database successfully.")
            return redirect('showmovies')
    else:    
        form = MovieForm()        
    return render(request,"testapp/addmovie.html",{'form':form})

def showmovies_view(request):
    movies = Movie.objects.all()
    return render(request, "testapp/showmovies.html", {'movies': movies})