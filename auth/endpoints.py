from tortoise import exceptions
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .backends.schemas import Token
from . import models, schemas, errors, crud

TAGS = ['auth']

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')
auth = APIRouter()


async def get_current_user(token: str = Depends(oauth2_scheme)) -> models.User:
    return await models.User.get_current_user(token)


@auth.post('/login', response_model=Token, tags=TAGS)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    try:
        user = await models.User.authenticate(
            username=form_data.username,
            password=form_data.password
        )
    except errors.AuthError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(err),
            headers={'WWW-Authenticate': 'Bearer'},
        )

    return user.create_token()


@auth.get('/user', response_model=schemas.User, tags=TAGS)
async def get_user(user: models.User = Depends(get_current_user)) -> models.User:
    return user


@auth.put('/user', response_model=schemas.User, tags=TAGS)
async def create_user(user: schemas.UserCreate) -> models.User:
    try:
        user = await crud.create(user)
    except exceptions.IntegrityError as err:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(err))

    return user


@auth.patch('/user', response_model=schemas.User, tags=TAGS)
async def update_user(update_data: schemas.UserUpdate, user: models.User = Depends(get_current_user)):
    return await crud.update(user, update_data)


@auth.delete('/user', tags=TAGS)
async def delete_user(user: models.User = Depends(get_current_user)):
    await user.delete()
    return {
        'status': 'ok',
    }
