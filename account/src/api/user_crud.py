from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User

async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)

async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)

async def create_user(session: AsyncSession, new_user: User) -> User | None:
    user = User(**new_user.model_dump())
    session.add(user)
    await session.commit()
    return user