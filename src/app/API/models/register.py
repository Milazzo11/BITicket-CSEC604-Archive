from .base import Auth
from fastapi import HTTPException
from pydantic import BaseModel, Field
from app.data.event import EventData
from app.data import event
from typing import Optional, List

from app.data.ticket import Ticket

class RegisterRequest(BaseModel):
    event_id: str = Field(..., description="ID of event to register for")
    verification: Optional[Auth[str]] = Field(None, description="Verification for non-public/paid events (user public key signed by event owner)")


class RegisterResponse(BaseModel):
    ticket: str = Field(..., description="Ticket string of registered user")

    @classmethod
    def generate(self, request: RegisterRequest, public_key: str) -> "RegisterResponse":
        """
        """

        event_data = EventData.load(request.event_id)

        if not event_data.event.private:
            ticket = Ticket.register(request.event_id, public_key)
            self.ticket = ticket.pack()

        elif request.verification is None:
            raise HTTPException(status_code=401, detail="No authorization")
        
        elif request.verification.public_key != event_data.data.owner_public_key:
            raise HTTPException(status_code=401, detail="Authorization key incorrect")

        else:
            request.verification.authenticate()
            
            ticket = Ticket.register(request.event_id, public_key)
            self.ticket = ticket.pack()

            