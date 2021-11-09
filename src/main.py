from fastapi import FastAPI, HTTPException
from src.pydantic_models.user import UserCreateModel, UserAuthModel
from src.database.user import add_user, authorization, get_meta_by_mail

app = FastAPI()


@app.post("/users/registration", status_code=201)
async def register_user(user: UserCreateModel):
    if get_meta_by_mail(user.email) is not None:
        raise HTTPException(status_code=403, detail="This mail has been already registered")
    success, msg = add_user(user.email, user.password.get_secret_value(), user.name, user.birth_date)
    if not success:
        raise HTTPException(status_code=403, detail=msg)
    return msg


@app.post("/users/auth")
async def authorize(user_auth: UserAuthModel):
    success, msg = authorization(user_auth.email, user_auth.password.get_secret_value())
    if not success:
        raise HTTPException(status_code=403, detail=msg)
    return success


