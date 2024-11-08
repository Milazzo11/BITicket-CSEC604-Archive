"""
High level API
"""


from app.API.models import *



def search_events(data: Auth[SearchRequest]) -> Auth[SearchResponse]:

    request = data.authenticate()
    response = SearchResponse.generate(request)

    return Auth[SearchResponse].load(response)


def create_event(data: Auth[CreateRequest]) -> Auth[CreateResponse]:

    request = data.authenticate()
    response = CreateResponse.generate(request, data.public_key)

    return Auth[CreateResponse].load(response)



def register_user(data: Auth[RegisterRequest]) -> Auth[RegisterResponse]:
    request = data.authenticate()
    response = RegisterResponse.generate(request, data.public_key)


    return Auth[RegisterResponse].load(response)




def cancel_ticket(data: Auth[CancelRequest]) -> Auth[CancelResponse]:
    request = data.authenticate()
    response = CancelResponse.generate(request, data.public_key)


    return Auth[CancelResponse].load(response)



def transfer_ticket(data: Auth[TransferRequest]) -> Auth[TransferResponse]:
    request = data.authenticate()
    response = TransferResponse.generate(request, data.public_key)


    return Auth[TransferResponse].load(response)


def redeem_ticket(data: Auth[RedeemRequest]) -> Auth[RedeemResponse]:
    request = data.authenticate()
    response = RedeemResponse.generate(request, data.public_key)

    return Auth[RedeemResponse].load(response)


def verify_redemption(data: Auth[VerifyRequest]) -> Auth[VerifyResponse]:
    request = data.authenticate()
    response = VerifyResponse.generate(request, data.public_key)

    return Auth[VerifyResponse].load(response)