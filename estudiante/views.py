from django.shortcuts import render


from .models import Curso

# Create your views here.

def estudiante(request):



    cursos=Curso.objects.all()

    return render(request, "estudiante/estudiante.html", {"cursos":cursos})