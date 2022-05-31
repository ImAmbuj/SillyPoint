from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()

    return render(request, 'index.html', {'blogs':blogs})

def blog(request, blog_id):
    blog = Blog.objects.filter(id= blog_id)
    
    return render(request,'blog.html',{'blog':blog[0]})    

def search(request):
    if request.method == "POST":
        search_key = request.POST['search_key']
        search_results = Blog.objects.filter(headline__contains = search_key)
        print(search_results)
    
        return render(request, 'search.html', {'search_results': search_results, 'searched': search_key})