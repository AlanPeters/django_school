from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Professor
# Create your views here.

def professors(request):
    professors_list = Professor.objects.order_by('-name')
    context = {
        'professors_list': professors_list,
    }
    return render(request, 'professors/index.html', context)

def detail(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    sections = professor.section_set.all()
    return render(request, 'professors/detail.html', {'professor': professor, 'sections': sections})
    


