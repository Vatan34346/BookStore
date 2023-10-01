from fastapi import APIRouter, Depends, status, HTTPException
from services import User_Service
from ..schemes import UserRegister, UserLogin
from ..repositories.auth import register
from helpers import hash_, jwt_handler


router = APIRouter(
    prefix='/v1/auth',
    tags=['Authentication']
)


@router.post('/login', status_code=status.HTTP_200_OK)
def login(request: UserLogin, db: User_Service = Depends(User_Service)):
    """Method for login which return JWT token for auth"""
    user = db.get_user('email', request.email)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')

    if not hash_.verify(request.password, user['password']):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials password or email')

    encoded_user = jwt_handler.sign_jwt(user)

    return {"access_token": encoded_user, "token_type": "bearer"}


@router.post('/register', status_code=status.HTTP_201_CREATED)
def registration(request: UserRegister, db: User_Service = Depends(User_Service)):
    """Creates new user"""
    new_user_data = {
        "email": request.email,
        "password": hash_.bcrypt(request.password),
        "name": request.name
    }
    id_ = register(db, new_user_data)
    return {
        "created_user_id": id_,
        "status": status.HTTP_201_CREATED
    }
