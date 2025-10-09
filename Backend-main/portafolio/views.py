from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def home(request):
    if request.method == "POST":
        return JsonResponse({"message": "Solicitud POST recibida correctamente"})
    return JsonResponse({"status": "OK"})
