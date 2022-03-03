from django.shortcuts import render
from .models import Post



def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    posts = Post.objects.get(id = pk)
    return render(request, 'post.html', {'posts':posts})

def input(request):
    if request.method == 'POST':
        detail = Post()
        detail.title = request.POST['title']
        detail.body = request.POST['detail']
        detail.save()
        return render(request, 'input.html')


    return render(request, 'input.html')
# Create your views here.
