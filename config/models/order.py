from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import Union, TYPE_CHECKING

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .product import Product


class Order(UserRelationMixin, Base):
    """Модель заказа
    """
    _user_back_populates = 'orders'

    promocode: Mapped[Union[str, None]] = mapped_column(nullable=True)
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now(),
                                                  server_default=func.now(),
                                                  )
    products: Mapped[list['Product']] = relationship(
        secondary='order_product_association',
        back_populates='orders',
    )
