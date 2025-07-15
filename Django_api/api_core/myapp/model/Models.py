from pydantic_mongo import PydanticObjectId
from pydantic import BaseModel, EmailStr, Field
from pydantic import field_serializer
from datetime import date
from enum import Enum

class CarModel(BaseModel):
    id: PydanticObjectId = None
    vehicle: str = Field(min_length=4)  
    rent_price_month: float = Field(default=0)  
    text : str = Field(min_length=6)

class ClientModel(BaseModel):
    id: PydanticObjectId = None
    name: str = Field(min_length=3)
    amount_pocketed: float | None = Field(default=None)
    deadline_to_apply: date | None = Field(input_value=date.today())
    email: EmailStr
    phone_number: str = Field(
        min_length=13,
        max_length=16,
        pattern=r'^\+\d{8,10}-\d{4}$',
        description="Phone number must be in the format +<DDI>83XXXX-XXXX (e.g., +55839999-9999)"
    )

    @field_serializer('deadline_to_apply')
    def serialize_date(self, deadline_to_apply, _info):
        if deadline_to_apply is None:
            return None
        return deadline_to_apply.isoformat()
        
class StatusEnum(str, Enum):
    FULL = "full deductible"
    PARTIAL = "partial deductible"
    THEFT = "Theft insurance"

class Insurance_policy(BaseModel):
    insurance_company: str = Field(min_length=3, max_length=35)
    deductible_type: StatusEnum = StatusEnum.PARTIAL
    deductible_amount: float = Field(default=0,gt=0)

class ContractModel(BaseModel):
    id: PydanticObjectId = None
    id_client: PydanticObjectId
    id_car: PydanticObjectId
    expires: date | None = Field(default=None)
    insurance_policy: Insurance_policy
        

    @field_serializer('expires')
    def serialize_date(self, expires, _info):
        if expires is None:
            return None
        return expires.isoformat()