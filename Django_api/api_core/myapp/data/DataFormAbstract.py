
from pydantic import BaseModel, EmailStr,Field
from datetime import date

class CarValidator(BaseModel):
    id: str = Field(min_length=12)
    vehicle: str = Field(min_length=4)  
    rent_price_month: float = Field(default=0)  
    text : str = Field(min_length=6)

class ClientValidator(BaseModel):
    id:None = Field(default=None)
    name: str = Field(min_length=3)
    amount_pocketed: float | None = Field(default=None)
    chosen_model: bool = Field(default=False)
    deadline_to_apply: date | None = Field(input_value=date.today())
    email: EmailStr
    phone_number: str = Field(
        min_length=13,
        max_length=16,
        pattern=r'^\+\d{8,10}-\d{4}$',
        description="Phone number must be in the format +<DDI>83XXXX-XXXX (e.g., +55839999-9999)"
    )