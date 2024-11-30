import uuid
import jwt
import requests
from datetime import datetime


class EventAPI:
    def __init__(self, private_key_path: str, public_key_path: str, base_url: str):
        """
        Initializes the EventAPI class with paths to keys and base URL.
        :param private_key_path: Path to the RSA private key file.
        :param public_key_path: Path to the RSA public key file.
        :param base_url: Base URL of the API.
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path
        self.base_url = base_url
        self.private_key = self._load_key(private_key_path)
        self.public_key = self._load_key(public_key_path)

    def _load_key(self, key_path: str) -> str:
        """Loads the key from the specified file path."""
        with open(key_path, "r") as key_file:
            return key_file.read()

    def _generate_jwt(self, data: dict) -> str:
        """Generates a JWT token for the given data."""
        return jwt.encode(data, self.private_key, algorithm="RS256")

    def _post_request(self, endpoint: str, payload: dict) -> requests.Response:
        """Sends a POST request to the specified endpoint with the given payload."""
        url = f"{self.base_url}/{endpoint}"
        return requests.post(url, json=payload)

    def search_event(self, text: str, limit: int, mode: str) -> requests.Response:
        """
        Sends a search request with a signed JWT.
        :param text: Text to search for.
        :param limit: Number of results to return.
        :param mode: Search mode (e.g., 'id', 'name').
        :return: Response from the server.
        """
        data = {
            "id": str(uuid.uuid4()),
            "timestamp": int(datetime.utcnow().timestamp()),
            "content": {"text": text, "limit": limit, "mode": mode},
        }
        signature = self._generate_jwt(data)
        payload = {"data": data, "public_key": self.public_key, "signature": signature}
        return self._post_request("search", payload)

    def register_user(self, event_id: str, content: str) -> requests.Response:
        """
        Sends a user registration request with a signed JWT.
        :param event_id: ID of the event the user is registering for.
        :param content: User-specific registration content.
        :return: Response from the server.
        """
        data = {
            "id": str(uuid.uuid4()),
            "timestamp": int(datetime.utcnow().timestamp()),
            "content": {"event_id": event_id, "verification": {}},
        }
        signature = self._generate_jwt(data)
        payload = {"data": data, "public_key": self.public_key, "signature": signature}
        return self._post_request("register", payload)

    def create_event(
        self,
        event_id: str,
        event_name: str,
        event_description: str,
        tickets: int,
        start: int,
        end: int,
        private: bool,
    ) -> requests.Response:
        """
        Sends a request to create an event with a signed JWT.
        :param event_id: Unique identifier for the event.
        :param event_name: Name of the event.
        :param event_description: Description of the event.
        :param tickets: Total number of tickets available for the event.
        :param start: Event start timestamp (Unix time).
        :param end: Event end timestamp (Unix time).
        :param private: Boolean indicating if the event is private.
        :return: Response from the server.
        """
        data = {
            "id": str(uuid.uuid4()),
            "timestamp": int(datetime.utcnow().timestamp()),
            "content": {
                "event": {
                    "id": event_id,
                    "name": event_name,
                    "description": event_description,
                    "tickets": tickets,
                    "issued": 0,
                    "start": start,
                    "end": end,
                    "exchanges": 16,
                    "private": private,
                }
            },
        }
        signature = self._generate_jwt(data)
        payload = {"data": data, "public_key": self.public_key, "signature": signature}
        return self._post_request("create", payload)

    def cancel_ticket(self, event_id: str, ticket: str) -> requests.Response:
        """
        Sends a ticket cancellation request with a signed JWT.
        :param event_id: ID of the event the ticket is associated with.
        :param ticket: Ticket ID or identifier to cancel.
        :return: Response from the server.
        """
        data = {
            "id": str(uuid.uuid4()),
            "timestamp": int(datetime.utcnow().timestamp()),
            "content": {"event_id": event_id, "ticket": ticket},
        }
        signature = self._generate_jwt(data)
        payload = {"data": data, "public_key": self.public_key, "signature": signature}
        return self._post_request("cancel", payload)


# Example usage
if __name__ == "__main__":
    # Initialize the API client
    api_client = EventAPI(
        private_key_path="../data/priv.key",
        public_key_path="../data/pub.key",
        base_url="http://localhost:8000",
    )

    # Search event
    search_response = api_client.search_event(text="event123", limit=1, mode="id")
    print("Search Response:", search_response.status_code, search_response.json())

    # Register user
    register_response = api_client.register_user(event_id="event123", content="user123")
    print("Register Response:", register_response.status_code, register_response.json())

    # Create event
    create_response = api_client.create_event(
        event_id="event123",
        event_name="Cybersecurity Conference",
        event_description="Annual cybersecurity conference.",
        tickets=500,
        start=int(datetime(2024, 12, 1, 9, 0).timestamp()),
        end=int(datetime(2024, 12, 1, 17, 0).timestamp()),
        private=False,
    )
    print("Create Event Response:", create_response.status_code, create_response.json())

    # Cancel ticket
    cancel_response = api_client.cancel_ticket(event_id="event123", ticket="ticket456")
    print(
        "Cancel Ticket Response:", cancel_response.status_code, cancel_response.json()
    )
