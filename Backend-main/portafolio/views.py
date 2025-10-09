from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
import requests
import json

@csrf_exempt
def home(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            nombre = data.get("nombre")
            correo = data.get("correo")
            mensaje = data.get("mensaje")

            # 📨 Datos del correo
            api_key = config("BREVO_API_KEY")
            destinatario = config("DEFAULT_FROM_EMAIL")  # tu correo destino
            asunto = f"Nuevo mensaje de {nombre}"
            contenido = f"De: {nombre} <{correo}>\n\n{mensaje}"

            # 🧩 Configurar payload
            url = "https://api.brevo.com/v3/smtp/email"
            headers = {
                "accept": "application/json",
                "api-key": api_key,
                "content-type": "application/json",
            }
            payload = {
                "sender": {"name": nombre, "email": correo},
                "to": [{"email": destinatario}],
                "subject": asunto,
                "textContent": contenido,
            }

            # 📤 Enviar correo a través de Brevo
            r = requests.post(url, headers=headers, json=payload)

            if r.status_code == 201:
                return JsonResponse({"success": True, "message": "Correo enviado correctamente"})
            else:
                return JsonResponse({"success": False, "error": r.text}, status=500)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"status": "OK"})
