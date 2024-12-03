"""
High level API
"""


from app.API.models import *



def search_events(data: Auth[SearchRequest]) -> Auth[SearchResponse]:

    print("h1")
    request = data.authenticate()

    print("h2")
    response = SearchResponse.generate(request)

    data = Data[SearchResponse].load(response)
    return Auth[SearchResponse].load(data)


def create_event(data: Auth[CreateRequest]) -> Auth[CreateResponse]:

    request = data.authenticate()
    response = CreateResponse.generate(request, data.public_key)
    
    data = Data[CreateResponse].load(response)
    return Auth[CreateResponse].load(data)



def register_user(data: Auth[RegisterRequest]) -> Auth[RegisterResponse]:
    request = data.authenticate()
    response = RegisterResponse.generate(request, data.public_key)

    data = Data[RegisterResponse].load(response)
    return Auth[RegisterResponse].load(data)




def cancel_ticket(data: Auth[CancelRequest]) -> Auth[CancelResponse]:
    request = data.authenticate()
    response = CancelResponse.generate(request, data.public_key)

    data = Data[CancelResponse].load(response)
    return Auth[CancelResponse].load(data)



def transfer_ticket(data: Auth[TransferRequest]) -> Auth[TransferResponse]:
    request = data.authenticate()
    response = TransferResponse.generate(request, data.public_key)

    data = Data[TransferResponse].load(response)
    return Auth[TransferResponse].load(data)


def redeem_ticket(data: Auth[RedeemRequest]) -> Auth[RedeemResponse]:
    request = data.authenticate()
    response = RedeemResponse.generate(request, data.public_key)

    data = Data[RedeemResponse].load(response)
    return Auth[RedeemResponse].load(data)


def verify_redemption(data: Auth[VerifyRequest]) -> Auth[VerifyResponse]:
    request = data.authenticate()
    response = VerifyResponse.generate(request, data.public_key)

    data = Data[VerifyResponse].load(response)
    return Auth[VerifyResponse].load(data)
