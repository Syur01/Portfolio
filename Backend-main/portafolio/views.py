import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings  # 🔹 importa settings

@csrf_exempt  # Permite peticiones desde Angular sin CSRF token
@require_http_methods(["POST", "GET"])
def home(request):
    if request.method == "OPTIONS":
        response = JsonResponse({"status": "ok"})
        response["Access-Control-Allow-Origin"] = "http://localhost:4200"  # o tu frontend deploy
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        return response

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            nombre = data.get("name", "Usuario")
            mensaje = data.get("message", "Mensaje vacío")
            remitente = data.get("email", "sin-correo")

            cuerpo = f"""
Nuevo mensaje del portafolio:

Nombre: {nombre}
Email: {remitente}
Mensaje:
{mensaje}
            """

            send_mail(
                "📩 Nuevo mensaje desde el portafolio",
                cuerpo,
                settings.DEFAULT_FROM_EMAIL,  # 🔹 usar DEFAULT_FROM_EMAIL
                ["bp113534@gmail.com"],       # destinatario
                fail_silently=False,
            )

            return JsonResponse({"status": "success", "message": "Correo enviado ✅"})

        except Exception as e:
            return JsonResponse({"status": "error", "detalle": str(e)}, status=500)

    return JsonResponse({"status": "ok", "message": "Backend en ejecución"})
