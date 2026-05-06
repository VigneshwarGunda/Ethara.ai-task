import uuid

from fastapi import APIRouter
from .. import schemas
from app.backend.database import cr, conn


router = APIRouter(tags=["Members"], prefix="/member")


@router.get("/all", response_model=list[schemas.ReturnLogin])

def get_all_memebers():
    return [
        {
            "id": str(uuid.uuid4()),
            "username": "john_doe",
            "phone": "1234567890",
            "gender": "male",
            "role": "developer"
        },
        {
            "id": str(uuid.uuid4()),
            "username": "jane_smith",
            "phone": "9876543210",
            "gender": "female",
            "role": "manager"
        }
    ]

    cr.execute("""SELECT * FROM users """)
    members = cr.fetchall()
    return members
