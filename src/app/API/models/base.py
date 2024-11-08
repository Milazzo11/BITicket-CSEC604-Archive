"""
"""

import time
from fastapi import HTTPException
from app.data.event import Event
from app.util import keys
from typing import List, Union, Generic, TypeVar, Optional
from pydantic import BaseModel, Field

import uuid

from app.crypto.asymmetric import AKE

from config import TIMESTAMP_ERROR

### encrypted ticktu must encrypt some punlic key data to validate owner



##### events probably should use an actual SQL DB

### managing bits in SQL seems easy too...




### REQUEST OBJECTS HANDLE PARSING LOGIC; RESPONSE HANDLE ACCESSING INTERNAL SERVER OPS
# <- move all this to __init__?



### TODO - tickets DO NOT NEED TO BE SEND ENCRYPTED -- BECAUSE THEY WILL ENCRYPT A PUBKEY
### SO EVEN IF ANOTHER USER GETS THE TICKET, IT WILL BE UNVERIFIABLE WITHOUT PRIVKEY ACCESS FOR SIGNATURES


### TODO - optional instead of union in crypto lib


### TODO - maybe figure out best Field conventions "..." vs. description= or just put the thing first


## TODO - ensure no white charactertics in vscode linting


### TODO - prob rework crypto libs to allow JWT and JWE for dict type (but do Union[bytes, str, dict] to generalize)



T = TypeVar("T")




class Data(BaseModel, Generic[T]):
    id: str = Field(..., description="Unique data transaction ID")###default_factory makes docs say this isn't required
    timestamp: float = Field(..., description="Epoch timestamp at send time")
    content: T = Field(..., description="Data contents")
    

    ### keep ID until message timestamp expire to prevent any form of replay attack

    @classmethod
    def load(self, content: T) -> "Data":
        """
        """

        return self(
            id=str(uuid.uuid4()), timestamp=time.time(),
            content=content
        )


class Auth(BaseModel, Generic[T]):
    data: Data[T] = Field(..., description="Authenticated data")
    public_key: str = Field(..., description="Public key (to verify signature)")
    signature: str = Field(..., description="Digital signature (JWT of the internal JSON data block)")


    @classmethod
    def load(self, data: Data[T]) -> "Auth":
        """
        """

        data_json = self.data.model_dump_json()
        cipher = AKE(private_key=keys.priv())

        return self(
            data=data, pubkey=keys.pub(),
            signature=cipher.sign(data_json)
        )
    


    def unwrap(self) -> T:
        return self.data.content


    def authenticate(self, challenge_verif: callable = lambda _: True) -> T:
        """
        """

        data_json = self.data.model_dump_json()
        cipher = AKE(public_key=self.public_key)

        ### TODO - ID validation at some point as well
        ### verify that ID is unique within timeframe to prevent replay
        ### call "challenge_verif" to confirm completion of additional complexity challenge (not to be implemented in this version)

        if not cipher.verify(self.signature, data_json):
            raise HTTPException(status_code=401, detail="Authentication failed")
        
        if abs(time.time() - self.data.timestamp) > TIMESTAMP_ERROR:
            raise HTTPException(status_code=401, detail="Timestamp sync failure")
        
        return self.data.content

        





























