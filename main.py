"""main file"""
from fastapi import Depends, FastAPI, HTTPException
from src.database.users import UsersDataBase
from src.pydantic_models.user import UserCreateModel
from src.pydantic_models.user import UserAuthModel

app = FastAPI()


def get_db():
    udb = UsersDataBase()
    yield udb


@app.post("/users/registration", status_code=201)
async def register_user(user: UserCreateModel, udb: UsersDataBase = Depends(get_db)):
    if udb.get_meta_by_mail(user.email) is not None:
        raise HTTPException(status_code=403,
                            detail="This mail has been already registered")
    success, msg = udb.add_user(user.email, user.password.get_secret_value(),
                                user.name, user.birth_date)
    if not success:
        raise HTTPException(status_code=403, detail=msg)
    return msg


@app.post("/users/auth")
async def authorize(user_auth: UserAuthModel, udb: UsersDataBase = Depends(get_db)):
    success, msg = udb.authorization(user_auth.email,
                                     user_auth.password.get_secret_value())
    if not success:
        raise HTTPException(status_code=403, detail=msg)
    return success
