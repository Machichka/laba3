from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.crud import crud_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return crud_user.create_user(user)

@router.get("/", response_model=list[UserResponse])
def read_users():
    return crud_user.get_users()

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    user = crud_user.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    updated = crud_user.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
def delete_user(user_id: int):
    deleted = crud_user.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "Deleted"}
