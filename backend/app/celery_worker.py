from cgitb import enable

from celery import Celery
from celery.utils.time import timezone

from app.config import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

celery_app = Celery(
    "petzone",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/Chisinau",
    enable_utc=True,
)

@celery_app.task(bind=True, max_reties=3)
def add(self, to_email: str, subject: str, message: str, is_html: bool = False):
    try:
        msg = MIMEMultipart()
        msg["From"] = settings.FROM_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        if is_html:
            msg.attach(MIMEText(message, "html"))
        else:
            msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            if settings.SMTP_USER and settings.SMTP_PASSWORD:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)

        logger.info(f"Email sent successfully to {to_email}")
        return {"status": "success", "message": f"Email sent to {to_email}"}

    except Exception as e:
        logger.error(f"Failed to send email to {to_email}: {str(e)}")
        raise self.retry(countdown=60, exc=e)

