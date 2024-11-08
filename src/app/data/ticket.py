
from pydantic import BaseModel, Field
from typing import Optional

from .storage import ticket as ticket_db


class Ticket(BaseModel):
    event_id: str
    public_key: str
    number: int


    @classmethod
    def register(self, event_id, public_key, number: Optional[int] = None) -> "Ticket":###maybe return ticket object
        
        ### TODO - implement

        ## fetch event by ID (and ensure ticket slots still remail)

        ## update database ** (change redemption bit string)

        ## generate ticket string
        
        ## return

        return self(
            event_id=event_id, public_key=public_key, number=0 ## MAKE THIS THE REAL THING LATER
        )


    @classmethod
    def load(self, event_id: str, ticket: str) -> "Ticket":
        """
        """
        ### probably turn this into like "events.ticket" or something

        # maybe keep this file just for ticket obj that converts from ticket str to obj and vice versa
        ## but events should prob just use it, not API directly
        ### TODO - implement

        return self(
            event_id=event_id, public_key="", number=0 ## MAKE THIS THE REAL THING LATER
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
    

    def redeem(self) -> None:
        pass
        ## this should be part of Ticket
        ## throw an error on failure
        ### TODO - implement


    def pack(self) -> str:
        """
        Convert ticket data to encrypted string.
        """
        ### TODO - implement


    def verify(self):
        pass
        ### TODO - implement


### thought -- ticket stuff seems logical to use OOP (since everything ticket related can just be handled in here)




### TODO - does this rly deserve to be its own file? -- it's basically just event.searching then getting ticket
### ## 6 yes, keep it -- and then have a separate data module