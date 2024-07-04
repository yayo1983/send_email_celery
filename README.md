my_fastapi_project/
│
├── main.py
├── celery_app.py
└── tasks.py

docker-compose up --build

## Probar la API

curl -X POST "http://localhost:8000/send-email/" -H "Content-Type: application/json" -d '{"email": "test@example.com", "subject": "Hello", "body": "This is a test email."}'

