from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, database, schemas

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(database.get_db)):
    return crud.get_all_users(db)
