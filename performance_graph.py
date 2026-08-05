import hashlib
import time
import secrets
import matplotlib.pyplot as plt

# Simulated relative cost model:
# Full PQC authentication (Dilithium + Kyber) is computationally heavier
# than lightweight hash-based re-authentication. Since implementing full
# lattice-based cryptography was outside scope, we model this using
# repeated hash rounds as a computational-cost proxy.

FULL_AUTH_ROUNDS = 3000   # simulates heavier PQC-style computation
REAUTH_ROUNDS = 50        # simulates lightweight hash verification

def simulate_full_authentication(drone_id):
    start = time.time()
    data = drone_id + secrets.token_hex(16)
    key = data.encode()
    for _ in range(FULL_AUTH_ROUNDS):
        key = hashlib.sha256(key).digest()
    end = time.time()
    return end - start, key.hex()

def simulate_reauthentication(drone_id, session_key):
    start = time.time()
    token = session_key.encode()
    for _ in range(REAUTH_ROUNDS):
        token = hashlib.sha256(token).digest()
    end = time.time()
    return end - start

full_times = []
reauth_times = []
drone_id = "drone_01"

for i in range(10):
    t_full, session_key = simulate_full_authentication(drone_id)
    full_times.append(t_full)
    t_reauth = simulate_reauthentication(drone_id, session_key)
    reauth_times.append(t_reauth)

avg_full = sum(full_times) / len(full_times)
avg_reauth = sum(reauth_times) / len(reauth_times)
reduction = ((avg_full - avg_reauth) / avg_full) * 100

print(f"Average Full Authentication Time: {round(avg_full, 6)} seconds")
print(f"Average Re-authentication Time: {round(avg_reauth, 6)} seconds")
print(f"Overhead Reduction: {round(reduction, 2)}%")

x = range(1, 11)
plt.plot(x, full_times, label="Full Authentication (PQC-simulated)", marker='o')
plt.plot(x, reauth_times, label="Lightweight Re-authentication", marker='o')
plt.xlabel("Authentication Attempts")
plt.ylabel("Time (seconds)")
plt.title("Authentication Time Comparison")
plt.legend()
plt.savefig("performance_comparison.png", dpi=150, bbox_inches='tight')
<<<<<<< HEAD
plt.show()
=======
plt.show()
>>>>>>> 33bbf0a89883e8474c3247274fb9abe794fd3d61
