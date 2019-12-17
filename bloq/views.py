from django.shortcuts import render

# Create your views here.
def post_list(therequest):
    localvar1 = render(therequest, 'bloq/pos_lsit.html', {})
    print(localvar1)
    return localvar1