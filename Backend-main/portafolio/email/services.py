import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from decouple import config

def enviar_correo(nombre, email, mensaje):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = config('BREVO_API_KEY')

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    email_data = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": "bp113534@gmail.com"}],  # tu correo receptor
        sender={"email": config("DEFAULT_FROM_EMAIL"), "name": nombre},
        subject=f"Nuevo mensaje de {nombre}",
        html_content=f"""
        <h3>Nuevo mensaje de contacto</h3>
        <p><b>Nombre:</b> {nombre}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>Mensaje:</b> {mensaje}</p>
        """
    )

    try:
        api_instance.send_transac_email(email_data)
        return True
    except ApiException as e:
        print(f"Error enviando correo: {e}")
        return False
