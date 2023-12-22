from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from asignaciondecursos.asignaciondecursos import Asignaciondecursos
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .models import Asignacion
from asignacion.models import LineaAsignacion, Asignacion

# Create your views here.

@login_required(login_url="/registrarse/logear")
def procesar_asignacion(request):
    asignacion=Asignacion.objects.create(user=request.user)
    asignaciondecursos=Asignaciondecursos(request)
    lineas_asignacion=list()
    for key, value in asignaciondecursos.asignaciondecursos.items():
        lineas_asignacion.append(LineaAsignacion(

            curso_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            asignacion=asignacion
        ))

    LineaAsignacion.objects.bulk_create(lineas_asignacion)

    enviar_mail(

            asignacion=asignacion,
            lineas_asignacion=lineas_asignacion,
            nombreusuario=request.user.username,
            email_usuario=request.user.email
    )

    messages.success(request, "Su asignacion a sido exitosa")

    return redirect("/estudiante")
    
    

def enviar_mail(**kwargs):

    asunto="Asignacion Exitosa"
    mensaje=render_to_string("emails/asignacion.html",{

        "asignacion": kwargs.get("asignacion"),
        "lineas_asignacion": kwargs.get("lineas_asignacion"),
        "nombreusuario":kwargs.get("nombreusuario")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="tu correo"
    to=kwargs.get("email_usuario")
    #to="emalez20@gmail.com"

    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)


