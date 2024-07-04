from celery_worker import celery
import time

@celery.task
def send_email(to_email: str, subject: str, body: str):
    # Simulación de envío de correo
    time.sleep(5)
    print(f"Correo enviado a {to_email} con asunto '{subject}'")
    return f"Correo enviado a {to_email} con asunto '{subject}'"
