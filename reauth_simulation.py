import hashlib
import time
import secrets

def full_authentication(drone_id):

    data = drone_id + secrets.token_hex(16)
    session_key = hashlib.sha256(data.encode()).hexdigest()

    return session_key


def reauthentication(drone_id, session_key):

    start = time.time()

    token = hashlib.sha256((drone_id + session_key).encode()).hexdigest()
    verify = hashlib.sha256((drone_id + session_key).encode()).hexdigest()

    end = time.time()

    if token == verify:
        print("Re-authentication successful")

    print("Re-authentication time:", round(end - start, 6), "seconds")


drone_id = "drone_01"

session_key = full_authentication(drone_id)

print("Drone reconnects...\n")

reauthentication(drone_id, session_key)
