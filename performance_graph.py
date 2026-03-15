import hashlib
import time
import secrets
import matplotlib.pyplot as plt

full_times = []
reauth_times = []

drone_id = "drone_01"

for i in range(10):

    start = time.time()

    data = drone_id + secrets.token_hex(16)
    session_key = hashlib.sha256(data.encode()).hexdigest()

    end = time.time()
    full_times.append(end - start)

    start = time.time()

    token = hashlib.sha256((drone_id + session_key).encode()).hexdigest()
    verify = hashlib.sha256((drone_id + session_key).encode()).hexdigest()

    end = time.time()
    reauth_times.append(end - start)


x = range(1, 11)

plt.plot(x, full_times, label="Full Authentication")
plt.plot(x, reauth_times, label="Lightweight Re-authentication")

plt.xlabel("Authentication Attempts")
plt.ylabel("Time (seconds)")
plt.title("Authentication Time Comparison")

plt.legend()
plt.show()
