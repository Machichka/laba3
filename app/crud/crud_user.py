from typing import Dict
from app.schemas.user import UserCreate, UserUpdate

fake_db: Dict[int, dict] = {}
current_id = 1

def create_user(user: UserCreate):
    global current_id
    new_user = user.dict()
    new_user["id"] = current_id
    fake_db[current_id] = new_user
    current_id += 1
    return new_user

def get_users():
    return list(fake_db.values())

def get_user(user_id: int):
    return fake_db.get(user_id)

def update_user(user_id: int, user: UserUpdate):
    if user_id not in fake_db:
        return None
    stored = fake_db[user_id]
    update_data = user.dict(exclude_unset=True)
    stored.update(update_data)
    return stored

def delete_user(user_id: int):
    return fake_db.pop(user_id, None)
