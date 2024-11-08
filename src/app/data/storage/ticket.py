

def register(event_id: str, ticket_number: int) -> int:
    """
    """
    ### This doesn't need a bitstring... literally just increment and return remaining ticket count




### transfer doesn't need to change registration count data


## during transfer: if a ticket is returned, how can the server actually reuse it?
#### no matter what, exchange bits are incremented to invalidate old ticket

## 0 1 2 3 4 5 6 7 8 9
#      *
### IDEA: set "exchanged" bit



def cancel(event_id: str, ticket_number: int) -> bool:
    """
    """
    


def redeem(event_id: str, ticket_number: int) -> bool:
    """
    """