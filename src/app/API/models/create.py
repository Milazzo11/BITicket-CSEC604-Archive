from pydantic import BaseModel, Field
from app.data.event import Event
from typing import List, Optional



class CreateRequest(BaseModel):
    event: Event = Field(..., description="New event to create on server")

    def to_dict(self) -> dict:
        return {
            "event": self.event.to_dict()
        }
    

class CreateResponse(BaseModel):
    event_id: Optional[str] = Field(None, description="New event ID (if successfully created)")

    @classmethod
    def generate(self, request: CreateRequest, public_key: str) -> "CreateResponse":
        """
        """

        event_id = request.event.create(public_key)
        ## TODO -- event ID doesn't return

        return self(event_id=event_id)
    

    def to_dict(self) -> dict:
        return self.__dict__