import hashlib
import time
import secrets

def full_authentication(drone_id):

    print("Drone:", drone_id, "sending authentication request...")

    start = time.time()

    data = drone_id + secrets.token_hex(16)
    session_key = hashlib.sha256(data.encode()).hexdigest()

    end = time.time()

    print("Server: Session key generated")
    print("Authentication time:", round(end - start, 6), "seconds")

    return session_key


drone_id = "drone_01"

session_key = full_authentication(drone_id)

print("\nSession established")
print("Session Key:", session_key)
