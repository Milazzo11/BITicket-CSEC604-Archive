from .base import Auth
from pydantic import BaseModel, Field
from app.data.event import Event
from app.util import keys
from typing import List, Optional
from fastapi import HTTPException

from app.data.ticket import Ticket



class Transfer(BaseModel):
    ticket: str = Field(..., description="Ticket being transferred")
    transfer_public_key: str = Field(..., description="Public key of the new ticket owner (user making request)")


class TransferRequest(BaseModel):
    event_id: str = Field(..., description="ID of the event for which the ticket is being transferred")
    transfer: Auth[Transfer] = Field(..., description="Transfer authorization JSON (signed by current ticket owner)")


class TransferResponse(BaseModel):
    ticket: str = Field(..., description="New ticket string transferred to user")

    @classmethod
    def generate(self, request: TransferRequest, public_key: str) -> "TransferResponse":
        """
        """

        transfer_data = request.transfer.unwrap()

        if transfer_data.transfer_public_key != public_key:
            raise HTTPException(status_code=401, detail="Authorization key incorrect")
        
        old_ticket = Ticket.load(request.event_id, transfer_data.ticket)

        if request.transfer.public_key != old_ticket.public_key:
            raise HTTPException(status_code=401, detail="Authorization key incorrect")

        request.transfer.authenticate()

        new_ticket = Ticket.register(
            request.event_id, public_key, number=old_ticket.number
        )
        self.ticket = new_ticket.pack()