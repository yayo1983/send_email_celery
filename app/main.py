from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, EmailStr
from tasks import send_email

app = FastAPI()

class EmailSchema(BaseModel):
    email: EmailStr
    subject: str
    body: str

@app.post("/send-email/")
def send_email_endpoint(email: EmailSchema, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email.delay, email.email, email.subject, email.body)
    return {"message": "Correo en proceso de envío"}
