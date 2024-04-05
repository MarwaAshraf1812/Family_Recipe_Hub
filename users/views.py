from django.shortcuts import render


# this is dummy function only to check if it works or not.
def dummy(request):
    return render(request, 'base.html')
