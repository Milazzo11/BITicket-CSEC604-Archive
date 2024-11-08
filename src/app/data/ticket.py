
from pydantic import BaseModel, Field
from typing import Optional

from .storage import ticket as ticket_db
from .event import EventData


from app.crypto.symmetric import SKE

from fastapi import HTTPException


class Ticket(BaseModel):
    event_id: str
    public_key: str
    number: int
    event_data: EventData

    @classmethod
    def register(self, event_id, public_key, number: Optional[int] = None) -> "Ticket":###maybe return ticket object
        
        event_data = EventData.load(event_id)

        if number is None:
            number = event_data.event.next_ticket()

        ticket_db.register(event_id, number)

        # <<describe better>> load data, increment ticket/verify, change database to reflect increment

        return self(
            event_id=event_id,
            public_key=public_key,
            number=number,
            event_data=event_data
        )


    @classmethod
    def load(self, event_id: str, ticket: str) -> "Ticket":
        """
        """

        event_data = EventData.load(event_id)

        data = self.event_data.data
        cipher = SKE(key=data.event_key)

        decrypted_ticket_raw = cipher.decrypt(ticket)
        ticket_data = decrypted_ticket_raw.split(" ")

        if ticket_data[0] != event_id:
            raise HTTPException(status_code=401, detail="Ticket data does not match event ID")
            # ensure ticket event ID matches the event ID passed by client
        
        return self(
            event_id=event_id,
            public_key=ticket_data[1],
            number=ticket_data[2],
            event_data=event_data
        )



    def cancel(self) -> None:
        """
        """
        ### cancel (return) a ticket
        ### TODO - actually deal with return logic
        #
        # --- have a list of returned tickets; these tickets will be reissued with precedence; create a max list size (invalidate return if over)
        # authenticated ticket return (write down somewhere):
        # - user returns ticket to event owner
        # - event owner can then obviously verify ticket return
        # - event owner returns ticket to server
        #
        # ^^ this also solves TICKET_QUEUE_PROBLEM -- users can always transfer tickets back to owner
        ###  and then the owner can fill the queue up with requests as it empties (prevents server misuse, but still doesn't annoy clients)

        ### NEXT_TICKET in events just needs to be updated, with that added list
        #### might actually move that func to DATA
    

    def redeem(self) -> None:
        pass
        ## this should be part of Ticket
        ## throw an error on failure
        ### TODO - implement


    def pack(self) -> str:
        """
        Convert ticket data to encrypted string.
        """

        data = self.event_data.data
        cipher = SKE(key=data.event_key)

        ticket_string_raw = self.event_id + " " + self.public_key + " " + self.number
        encrypted_string = cipher.encrypt(ticket_string_raw)

        ticket_string = cipher.iv_b64() + "-" + encrypted_string

        return ticket_string


    def verify(self):
        pass
        ### TODO - implement


### thought -- ticket stuff seems logical to use OOP (since everything ticket related can just be handled in here)




### TODO - does this rly deserve to be its own file? -- it's basically just event.searching then getting ticket
### ## 6 yes, keep it -- and then have a separate data module