
from fastapi import HTTPException
from app.data.event import Event
from typing import List, Union, Generic, TypeVar, Optional
from pydantic import BaseModel, Field

from app.data.ticket import Ticket


class RedeemRequest(BaseModel):
    event_id: str = Field(..., description="ID of the event for which the ticket is being redeemed")
    ticket: str = Field(..., description="Ticket being redeemed")



class RedeemResponse(BaseModel):
    success: bool = Field(True, description="Ticket redemption status")

    @classmethod
    def generate(self, request: RedeemRequest, public_key: str) -> "RedeemResponse":
        """
        """

        ticket = Ticket.load(request.event_id, request.ticket)
        
        if ticket.public_key != public_key:
            raise HTTPException(status_code=401, detail="Authorization key incorrect")
        
        ticket.redeem() ## throws err on failure