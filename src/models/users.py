from pydantic import BaseModel, EmailStr
from .events import Event

class User(BaseModel): # db에 실제로 들어가는 테이블
    email: EmailStr
    password: str
    events: list[Event] | None = None

class UserSingIn(BaseModel):# 유저가 로그인 할 때 정보를 제대로 기입 하는지
    email : EmailStr
    password : str