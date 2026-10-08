from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_db
from .. import crud, schemas

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("/", response_model=List[schemas.CustomerOut])
async def get_customers(db: AsyncSession = Depends(get_db)):
    return await crud.list_customers(db)

@router.post("/", response_model=schemas.CustomerOut, status_code=status.HTTP_201_CREATED)
async def post_customer(customer: schemas.CustomerCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_customer(db, customer)
