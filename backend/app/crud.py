from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def create_customer(db: AsyncSession, customer_in: schemas.CustomerCreate):
    obj = models.Customer(**customer_in.dict())
    db.add(obj)
    await db.flush()
    await db.commit()
    await db.refresh(obj)
    return obj

async def list_customers(db: AsyncSession, limit: int = 100):
    q = await db.execute(select(models.Customer).limit(limit))
    return q.scalars().all()
