from django.shortcuts import render
from django.utils import timezone
from .models import MyBlogPost

# Create your views here.
def post_list(therequest):
    post_lidt = MyBlogPost.objects.filter(thepublishdate__lte = timezone.now()).order_by('mytitle')
    localvsr1 = render(therequest, 'bloq/pos_lsit.html', {"psots":post_lidt})
    print(localvsr1)
    return localvsr1