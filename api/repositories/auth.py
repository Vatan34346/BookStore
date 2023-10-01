from services import User_Service
from fastapi import HTTPException, status


def register(db: User_Service, data):
    created_user_id = db.create_user(data)
    if not created_user_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'User already exists')
    return created_user_id



