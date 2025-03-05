import json
from helpers import cryptography

class RaffleTicket:
    def __init__(self, ownerPublicKey, number, raffleHash):
        self.ownerPublicKey = ownerPublicKey
        self.number = number
        self.raffleHash = raffleHash

    def hash(self):
        payload = {
            'ownerPublicKey': self.ownerPublicKey,
            'number': self.number,
            'raffleHash': self.raffleHash
        }
        payload_string = json.dumps({k: str(v) for k, v in payload.items()}, sort_keys=True)
        return cryptography.hash_string(payload_string)