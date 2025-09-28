from django.shortcuts import render

## Creating a function post_list to take requests and return informaiton from another function.
def post_list(request):
    return render(request, 'blog/post_list.html', {})