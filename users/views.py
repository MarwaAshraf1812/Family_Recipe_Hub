from django.shortcuts import render



def dummy(request):
    return render(request, 'base.html', name='dummy')
