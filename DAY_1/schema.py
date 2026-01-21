from pydantic import BaseModel

class item(BaseModel):
    name: str
    description: str | None = None
    price: float
    in_stock: bool = True