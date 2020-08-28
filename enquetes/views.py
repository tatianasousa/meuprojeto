from django.shortcuts import render
from enquetes.models import Enquete

def bemvindo(request):
    return render(request, 'bemvindo.html')
def exibir (request, enquete_id):
    enquete = Enquete()
    if enquete_id == 1:
        enquete = Enquete(1, 'Qual é o seu nome?', '28/08/2020')
    if enquete_id == 2:
        enquete = Enquete(2, 'Qual é a sua idade?', '28/08/2020')
    if enquete_id == 3:
        enquete = Enquete(3, 'Onde você mora?', '28/08/2020')
    return render(request, 'enquete.html', {"enquete":enquete})
