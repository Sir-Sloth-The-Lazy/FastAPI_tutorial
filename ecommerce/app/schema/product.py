from pydantic import BaseModel, Field
from typing import Annotated, Literal
from uuid import UUID

class Product(BaseModel):
    id : UUID
    sku : Annotated[
        str,
        Field(max_length=36, min_length=6, title="SKU", description="Stock Keeping Unit", examples=["e75-h43-700" , "as0-89r-456"])
    ]
    name : Annotated[str, Field(min_length=3, max_length=80, title="Product Name", description="Readable Product Name", examples=["Xiaomi Model X" , "Apple iPhone 12"])]
    description : Annotated[
        str,
        Field(max_length=200, description="Short product description")
    ]
    category: Annotated[
        str,
        Field(min_length=3, max_length=30, description="Catoegory like mobiles/laptops/accessories", examples=["mobiles", "laptops"])
    ]
    brand : Annotated[
        str,
        Field(min_length=2, max_length=40, examples=["Xaiomi", "Apple"])
    ]
    price : Annotated[
        float,
        Field(gt=0, strict=True, description="Base price (INR)")
    ]
    currency : Literal["INR"] = "INR"
    discount_percent : Annotated[
        int,
        Field(ge=0, le=90, description="Discount in Percentage")
    ] = 0
    