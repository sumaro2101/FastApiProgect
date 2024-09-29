from pydantic import BaseModel, ConfigDict, Field
from typing import Union


class ProductBase(BaseModel):
    """Схема товара
    """
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: str
    price: int


class ProductUpdate(BaseModel):
    """Обновление товара
    """
    model_config = ConfigDict(from_attributes=True)

    name: Union[str, None] = Field(default=None)
    description: Union[str, None] = Field(default=None)
    price: Union[int, None] = Field(default=None)


class ProductCreate(ProductBase):
    """Создание продукта
    """
    model_config = ConfigDict(from_attributes=True)


class Product(ProductBase):
    """Схема товара с ID
    """
    model_config = ConfigDict(from_attributes=True)

    id: int
