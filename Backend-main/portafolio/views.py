from django.http import JsonResponse
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        try:
            nombre = request.POST.get("nombre", "Usuario")
            mensaje = request.POST.get("mensaje", "Mensaje vacío")
            remitente = request.POST.get("email", "sin-correo")

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
                None,  # Usa DEFAULT_FROM_EMAIL
                ["bp113534@gmail.com"],  # destinatario real
                fail_silently=False,
            )

            return JsonResponse({"status": "success", "message": "Correo enviado"})
        except Exception as e:
            return JsonResponse({"status": "error", "detalle": str(e)})

    return JsonResponse({"status": "ok", "message": "Backend en ejecución"})
