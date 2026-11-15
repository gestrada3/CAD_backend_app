from pydantic import BaseModel, constr, condecimal


# Pydantic schema constraints
class ItemBase(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: constr(max_length=255) | None = None
    price: condecimal(
                gt=0.0, max_digits=10, decimal_places=2
            )


# Schema for creating a new item
class ItemCreate(ItemBase):
    pass


# Schema for reading/returning an item (includes id)
class Item(ItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
