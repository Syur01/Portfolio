from django.http import JsonResponse
import json
from .email.services import enviar_correo

def contacto(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nombre = data.get("nombre")
        email = data.get("email")
        mensaje = data.get("mensaje")

        exito = enviar_correo(nombre, email, mensaje)

        if exito:
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False}, status=500)
