def importe_total_asignaciondecursos(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["asignaciondecursos"].items():
            total=total+float(value["precio"])
    
    else:
        total="Debes hacer login"

    return{"importe_total_asignaciondecursos":total}