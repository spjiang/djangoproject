from django.shortcuts import render
from myblog.models import BlogPost
# Create your views here.
def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')[:5]
    return render(request,'archive.html',{'posts':posts})