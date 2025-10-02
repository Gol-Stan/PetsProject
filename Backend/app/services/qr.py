import qrcode
import uuid
from pathlib import Path


QR_FOLDER = Path("/static/qr_codes")
QR_FOLDER.mkdir(parents=True, exist_ok=True)


def generate_code(pet_id: int) -> str:
    qr_code = str(uuid.uuid4())
    url = f"https://localhost:8000/pets/qr/{qr_code}"

    img = qrcode.make(url)
    file_path = QR_FOLDER / f"{qr_code}.png"
    img.save(file_path)

    return qr_code