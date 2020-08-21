from django.shortcuts import render

def bemvindo(request):
    return render(request, 'bemvindo.html')
