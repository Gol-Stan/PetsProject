from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel, EmailStr
from app.celery_worker import send_welcome_message



router = APIRouter(prefix="/email", tags=["email"])

class EmailRequest(BaseModel):
    email: EmailStr
    name: str

@router.post("/send-welcome")
async def send_welcome_endpoint(request: EmailRequest):
    try:
        task = send_welcome_message.delay(
            user_email=request.email,
            user_name=request.name
        )
        return {"message": "Welcome", "task_id": task.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to queue email: {str(e)}")