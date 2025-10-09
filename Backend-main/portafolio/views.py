from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .email.services import enviar_correo

@csrf_exempt
def home(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            nombre = data.get("nombre")
            correo = data.get("correo")
            mensaje = data.get("mensaje")

            if not nombre or not correo or not mensaje:
                return JsonResponse({"error": "Faltan campos obligatorios"}, status=400)

            exito = enviar_correo(nombre, correo, mensaje)

            if exito:
                return JsonResponse({"success": True, "message": "Correo enviado correctamente"})
            else:
                return JsonResponse({"success": False, "error": "No se pudo enviar el correo"}, status=500)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"status": "OK"})
