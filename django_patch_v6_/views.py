from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from.models import Post
from django.utils import timezone
# Create your views here.
'''a dot means current directory views and models are in the same directory so we can just import the name without ,py extension
To take actual blogpost from post we need querysets here is where we use query sets.
'''

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'post_list.html',{'posts':posts})



