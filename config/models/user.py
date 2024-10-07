from datetime import datetime
from typing import Union, TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, func
from sqlalchemy.types import LargeBinary

from config.models import Base

if TYPE_CHECKING:
    from .post import Post
    from .profile import Profile
    from .basket import Basket


class User(Base):
    """Модель пользователя
    """
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    password: Mapped[str] = mapped_column(LargeBinary)
    active: Mapped[bool] = mapped_column(default=True)

    posts: Mapped[list['Post']] = relationship(back_populates='user')
    profile: Mapped['Profile'] = relationship(back_populates='user')
    basket: Mapped['Basket'] = relationship(back_populates='user')
