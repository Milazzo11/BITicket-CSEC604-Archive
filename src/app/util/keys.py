from setup import PRIV_KEY_FILE, PUB_KEY_FILE


def priv() -> str:
    """
    """

    with open(PRIV_KEY_FILE, "rb") as f:
        pub_key = f.read()
        
    return pub_key.decode("utf-8")


def pub() -> str:
    """
    """
    
    with open(PUB_KEY_FILE, "rb") as f:
        pub_key = f.read()
        
    return pub_key.decode("utf-8")