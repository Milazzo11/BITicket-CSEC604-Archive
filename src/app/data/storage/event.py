"""
"""


from typing import List



### all of these should be simple SQL queries (complex logic happens outside this module)


#### TODO - I don't think using "event" and data objects here makes sense -- that logic can be dealt with at the obj level


def load(event_id: str) -> dict:###<-this funtionality will probably need to be split up
    """
    """
    ### Event return


def load_full(event_id: str) -> dict:###<-this funtionality will probably need to be split up
    """
    """
    ### EventData return



def search(text: str, limit: int) -> List[dict]:##these dicts are ONLY event, no data
    """
    """


def create(event: dict, event_data: dict) -> None:##prob pass data here too (OR maybe just make this a dict of event data)
    """
    """
    ## conversion from objects to DB (including weird intemediate steps) prob makes the most sense here


