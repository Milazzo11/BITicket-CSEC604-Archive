NOTE: CURRENTLY, STORAGE SYSTEM USES BYTES, NOT BITSTRINGS
### THIS IS JUST PROOF OF CONCEPT, BUT EVENTUALLY IMPLEMENT BITSTRINGS

... AND YA KNOW, TEST THE STUPID THING LOL

(MAKE SURE ALL HTTP STATUS CODES ACTUALLY MAKE THE MOST SENSE)
(AND MAKE IT SO THAT REQUEST SIGNATURE VERIF IS OF SUBSET)

uvicorn server:app --reload

TODO -
event search

add enpoints that will allow for creation of events
(so users can both create events and register)

also this could be made into an app



redemption -- no need to temporarily store pubkeys
- store ticket redemption status based on issue # in redemption bit-field
- in verify request, require event owner to pass (user's ticket + user's pubkey) <- not signed by user
  then server will return true/false
- tickets should be "stamped" once verified to indicate that a verification request was made



exchange -- REMOVE /CLAIM
- Bob provides Joseph with a JSON object containing his ticket and Joseph’s public key, then he signs this data to confirm a ticket transfer.
- Joseph completes the /transfer [his request payload contains his public key, the event ID, and Bob’s ticket transfer authorization JSON] → the server will verify the transfer request, invalidate Bob’s current ticket, and issue a new ticket to Joseph
- (can also create transfer AUTH JSON with empty transfer pubkey, then make /transfer request to return ticket)

-- later on, add expired event cleanup to setup and checks for that shit