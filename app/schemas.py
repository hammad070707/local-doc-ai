from pydantic import BaseModel,Field
from typing import List

class InvoiceItem(BaseModel):
    description:str=Field(description="Description of the invoice item")
    quantity:int=Field(description="Quantity of the invoice item")
    unit_price:float=Field(description="Unit price of the invoice item")
    amount:float=Field(description="Amount of the invoice item")

class InvoiceData(BaseModel):
    vendor_name: str = Field(description="Name of the supplier/vendor")
    invoice_number: str = Field(description="Invoice reference number")
    date: str = Field(description="Date of the invoice")
    items: List[InvoiceItem] = Field(description="List of items in the invoice")
    subtotal: float
    tax: float
    total_amount: float
    currency: str = Field(default="USD")

