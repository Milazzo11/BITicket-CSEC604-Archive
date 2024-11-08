from pydantic import BaseModel, Field
from app.data.event import Event
from typing import List, Optional
from fastapi import HTTPException

from app.data.ticket import Ticket


class VerifyRequest(BaseModel):
    event_id: str = Field(..., description="ID of the event to check user verification for")
    ticket: str = Field(..., description="Ticket string of user to check")
    check_public_key: str = Field(..., description="Public key of the user being checked for ticket redemption")



class VerifyResponse(BaseModel):
    success: bool = Field(True, description="User ticket redemption status")

    @classmethod
    def generate(self, request: VerifyRequest, public_key: str) -> "VerifyResponse":
        """
        """

        ticket = Ticket.load(request.event_id, request.ticket)

        if ticket.public_key != public_key:
            raise HTTPException(status_code=401, detail="Ticket invalid (non-matching key)")
        
        if request.event_id != ticket.event_id:
            raise HTTPException(status_code=401, detail="Ticket data does not match event ID")
        
        ticket.verify()## this should just raise HTTPException on error, not return 