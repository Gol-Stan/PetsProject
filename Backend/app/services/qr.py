import qrcode
import os
from uuid import uuid4

QR_FOLDER = "app/static/qr_codes"  # папка для хранения картинок QR-кодов
os.makedirs(QR_FOLDER, exist_ok=True)

def generate_code() -> str:
    return str(uuid4())

def save_qr_image(qr_code: str) -> str:
    img = qrcode.make(qr_code)
    file_path = os.path.join(QR_FOLDER, f"{qr_code}.png")
    img.save(file_path)
    return file_path